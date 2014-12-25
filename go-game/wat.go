package main

import (
	"fmt"
	"log"
	"github.com/gorilla/mux"
	"github.com/gorilla/websocket"
	"net/http"
	"time"
)

const (
	writeWait = 10 * time.Second
	pongWait = 60 * time.Second
	pingPeriod = (pongWait * 9) / 10
	maxMessageSize = 512
)

// send is the message from the hub we want to send to the websocket.
type connection struct {
	websocket *websocket.Conn
	send chan[] byte 
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
			if err := conn.write(websocket.TextMessage, message); err != nil {
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
	connections map[*connection]bool
	broadcast chan []byte
	register chan *connection
	unregister chan *connection
}

var globalHub = hub{
	broadcast:   make(chan []byte),
	register:    make(chan *connection),
	unregister:  make(chan *connection),
	connections: make(map[*connection]bool),
}

func (globalHub *hub) run() {
	numPlayers := 0
	for {
		select {
		case c := <-globalHub.register:
			globalHub.connections[c] = true
			numPlayers++
		case c := <-globalHub.unregister:
			if _, ok := globalHub.connections[c]; ok {
				delete(globalHub.connections, c)
				close(c.send)
				numPlayers--
			}
		case m := <-globalHub.broadcast:
			for c := range globalHub.connections {
				select {
				case c.send <-m:
				default:
					close(c.send)
					delete(globalHub.connections, c)
				}
			}
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

	conn := &connection{send: make(chan []byte, 256), websocket: wsConnection}
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
