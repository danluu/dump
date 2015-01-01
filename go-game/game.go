package main

import (
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/gorilla/websocket"
)

func assert(cond bool, message string) {
	if !cond {
		fmt.Println("assert failed: " + message)
	}
}

const (
	writeWait = 10 * time.Second
	pongWait = 60 * time.Second
	pingPeriod = (pongWait * 9) / 10
	maxMessageSize = 512
	numCards = 52
)

func popcount(x uint64) (n int) {
	x -= (x >> 1) & 0x5555555555555555
	x = (x>>2)&0x3333333333333333 + x&0x3333333333333333
	x += x >> 4
	x &= 0x0f0f0f0f0f0f0f0f
	x *= 0x0101010101010101
	return int(x >> 56)
}


type GameMessage struct {
	Message string
	Player int
	Cards []string
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

func cardSuitStr(card int) string {
	switch card {
	case 0: return "H"
	case 1: return "D"
	case 2: return "C"
	case 3: return "S"
	default: return "Suit Error"
	}
}

func serializeCard(card int) string {
	value := string(card / 4);
	suit := cardSuitStr(card);
	return value + suit;
}

func serializeHand(hand uint64) []string {
	handSize := popcount(hand)
	var handStr []string
	for i := 0; i < numCards; i++ {
		if hand & 1 == 1 {
			handStr = append(handStr, serializeCard(i))
		}
	}
	assert(handSize == len(handStr), "serializeHand handSize check")
	return handStr
}

type gameState struct {
	cardsWon []uint64
	center uint64
	hands []uint64
	numPlayers int
	started bool
}

var globalState = gameState{
	cardsWon: make([]uint64, 4),
	center: 0,
	hands: make([]uint64, 4),
	numPlayers: 0,
	started: false,
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
			}
		case c := <-all.unregister:
			if _, ok := all.connections[c]; ok {
				delete(all.connections, c)
				close(c.send)
			}
		case b := <-all.ready:
			cardOrder := rand.Perm(numCards)
			dealToPlayer := 0
			for i := 0; i < numCards; i++ {
				globalState.hands[dealToPlayer] |= 1 << uint(cardOrder[i])
				dealToPlayer = (dealToPlayer + 1) % 4;
			}
			if b {
				message := GameMessage{"start_game",0,[]string{}}
				sendToAll(*all, message)
			}
		case <-all.broadcast:
			m := GameMessage{"echo",0,[]string{}}
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
