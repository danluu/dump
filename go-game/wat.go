package main

import (
	"fmt"
	"log"
	"github.com/gorilla/mux"
	"github.com/gorilla/websocket"
	"net/http"
)

func HomeHandler(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "Hello, world!\n")
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
	
	conn, err := upgrader.Upgrade(response, request, nil)
	if err != nil {
		log.Println(err)
		return
	}

	for {
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			return
		}
		if err = conn.WriteMessage(messageType, p); err != nil {
			return // We should indicate an error somehow.
		}
	}
}

func main() {
	r := mux.NewRouter()

	r.PathPrefix("/").Handler(http.FileServer(http.Dir("./static/")))
	// r.PathPrefix("/echo").Handler(wsHandler)
	http.HandleFunc("/echo",wsHandler)
	http.Handle("/", r)


	// wait for clients
	http.ListenAndServe(":9999", nil)
}
