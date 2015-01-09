package main

import (
	"errors"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gorilla/mux"
	"github.com/gorilla/websocket"
)

const (
	writeWait      = 10 * time.Second
	pongWait       = 60 * time.Second
	pingPeriod     = (pongWait * 9) / 10
	maxMessageSize = 512
)

func assert(cond bool, message string) {
	if !cond {
		fmt.Println("assert failed: " + message)
	}
}

// TODO: add some type assertions to make sure we're not passing 
// bad messages around.
type Message interface {

}

type BrowserMessage struct {
	Message []byte
	Player  int
}

type GameMessage struct {
	Message string
	Player  int
	Cards   map[string]int
}

// This could be combined with GameMessage.
type LastActionMessage struct {
	Message string
	Player int
	Action []string
}

// send is the message from the hub we want to send to the websocket.
type connection struct {
	websocket *websocket.Conn
	send      chan Message
}

func (conn *connection) connectionId() (int, error) {
	for i, c := range globalHub.connections {
		if c == conn {
			return i, nil
		}
	}
	return -1, errors.New("Failed to find connection in list")
}

func (conn *connection) fromBrowser() {
	defer func() {
		globalHub.unregister <- conn
		conn.websocket.Close()
	}()
	conn.websocket.SetReadLimit(maxMessageSize)
	conn.websocket.SetReadDeadline(time.Now().Add(pongWait))
	conn.websocket.SetPongHandler(func(string) error { conn.websocket.SetReadDeadline(time.Now().Add(pongWait)); return nil })
	for {
		_, message, err := conn.websocket.ReadMessage()
		if err != nil {
			break
		}
		player, err := conn.connectionId()
		toProcess := BrowserMessage{message, player}
		globalHub.process <- toProcess
	}
}

func (conn *connection) write(messageType int, payload []byte) error {
	conn.websocket.SetWriteDeadline(time.Now().Add(writeWait))
	return conn.websocket.WriteMessage(messageType, payload)
}

// TODO: make this typecheck in some reasonable way?
func (conn *connection) writeJSON(message Message) error {
	conn.websocket.SetWriteDeadline(time.Now().Add(writeWait))
	return conn.websocket.WriteJSON(message)
}

func (conn *connection) toBrowser() {
	ticker := time.NewTicker(pingPeriod)
	defer func() {
		ticker.Stop()
		conn.websocket.Close()
	}()
	for {
		select {
		case message, ok := <-conn.send:
			if !ok {
				conn.write(websocket.CloseMessage, []byte{})
				return
			}
			if err := conn.writeJSON(message); err != nil {
				return
			}
		case <-ticker.C:
			if err := conn.write(websocket.PingMessage, []byte{}); err != nil {
				return
			}
		}
	}
}

type hub struct {
	connections []*connection
	process     chan BrowserMessage
	ready       chan bool
	register    chan *connection
	unregister  chan *connection
}

var globalHub = hub{
	connections: make([]*connection, 0),
	process:     make(chan BrowserMessage),
	ready:       make(chan bool),
	register:    make(chan *connection),
	unregister:  make(chan *connection),
}

func sendTo(all hub, message Message, player int) {
	select {
	case all.connections[player].send <- message:
	default: // TODO: handle error.
	}
}

func sendToAll(all hub, message Message) {
	for _, c := range all.connections {
		select {
		case c.send <- message:
		default:
			close(c.send)
			// Close connection somehow.
			// delete(all.connections, c)
		}
	}
}

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

func wsHandler(response http.ResponseWriter, request *http.Request) {
	if request.Method != "GET" {
		http.Error(response, "Method not allowed", 405)
		return
	}

	wsConnection, err := upgrader.Upgrade(response, request, nil)
	if err != nil {
		log.Println(err)
		return
	}

	conn := &connection{send: make(chan Message, 256), websocket: wsConnection}
	globalHub.register <- conn
	go conn.toBrowser()
	conn.fromBrowser()
}

func main() {
	go globalHub.run()

	r := mux.NewRouter()

	r.PathPrefix("/").Handler(http.FileServer(http.Dir("./static/")))
	http.HandleFunc("/echo", wsHandler)
	http.Handle("/", r)

	// wait for clients
	err := http.ListenAndServe(":9999", nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
