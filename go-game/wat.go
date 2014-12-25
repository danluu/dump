package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gorilla/mux"
	"github.com/gorilla/websocket"
)

const (
	writeWait = 10 * time.Second
	pongWait = 60 * time.Second
	pingPeriod = (pongWait * 9) / 10
	maxMessageSize = 512
)

type GameMessage struct {
	type string
	cards int
}

// send is the message from the hub we want to send to the websocket.
type connection struct {
	websocket *websocket.Conn
	send chan GameMessage
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
		globalHub.broadcast <- message
	}
}

func (conn *connection) write(messageType int, payload []byte) error {
	conn.websocket.SetWriteDeadline(time.Now().Add(writeWait))
	return conn.websocket.WriteMessage(messageType, payload)
}

func (conn *connection) writeJSON(message GameMessage) error {
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
	broadcast chan []byte
	connections map[*connection]bool
	ready chan bool
	register chan *connection
	unregister chan *connection
}

type gameState struct {
	started bool
	hands []uint64
}

var globalHub = hub{
	broadcast:   make(chan []byte),
	connections: make(map[*connection]bool),
	ready:       make(chan bool),
	register:    make(chan *connection),
	unregister:  make(chan *connection),
}

func sendToAll(all hub, message GameMessage) {
	for c := range all.connections {
		select {
		case c.send <- message:
		default:
			close(c.send)
			delete(all.connections, c)
		}
	}
}

func (all *hub) run() {
	numPlayers := 0
	for {
		select {
		case c := <-all.register:
			all.connections[c] = true
			numPlayers++
			if numPlayers == 2 {
				go func() {all.ready <- true;}() // This seems bad.
				fmt.Println("queued ready send")
			}
		case c := <-all.unregister:
			if _, ok := all.connections[c]; ok {
				delete(all.connections, c)
				close(c.send)
				numPlayers--
			}
		case b := <-all.ready:
			if b {
				message := GameMessage{"start_game",0}
				sendToAll(*all, message)
			}
		case <-all.broadcast:
			m := GameMessage{"echo",0}
			sendToAll(*all, m)
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

	conn := &connection{send: make(chan GameMessage, 256), websocket: wsConnection}
	globalHub.register <- conn
	go conn.toBrowser()
	conn.fromBrowser()
}

func main() {
	go globalHub.run()

	r := mux.NewRouter()

	r.PathPrefix("/").Handler(http.FileServer(http.Dir("./static/")))
	http.HandleFunc("/echo",wsHandler)
	http.Handle("/", r)

	// wait for clients
	http.ListenAndServe(":9999", nil)
}
