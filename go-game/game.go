package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"strconv"
)

const (
	maxCard = 12
)

// last is the last thing played, which needs to get sent to clients
// might not need/want it as part of state.
type gameState struct {
	currentPlayer int
	firstPass int
	hands []map[string]int
	last map[string]int
	numPlayers int
	started bool
}

var globalState = gameState{
	currentPlayer: 0,
	firstPass: -1,
	hands: make([]map[string]int, 10), // TODO: fix this 10
	last: make(map[string]int),
	numPlayers: 0,
	started: false,
}

func makeDeck() []string {
	deck := make([]string, 0)
	// Put cards into deck to be shuffled.
	for i := 0; i <= maxCard; i++ {
		if (i == 0) { 
			// TODO: wildcards.
		} else {
			// Deal out i cards of value i
			for j := 0; j < i; j++ {
				deck = append(deck, strconv.Itoa(i));
			}
		}
		
	}
	return deck
}

func shuffleDeck(deck []string) []string {
	shuffledDeck := make([]string, len(deck))
	perm := rand.Perm(len(deck))
	for i, v := range perm { shuffledDeck[v] = deck[i] }
	return shuffledDeck
}

func dealDeck(state *gameState, deck[]string, numPlayers int) {
	// Initialize unitialized maps in array of hands.
	for i := 0; i < numPlayers; i++ {
		state.hands[i] = make(map[string]int)
		for j := 0; j < maxCard+1; j++ {
			state.hands[i][strconv.Itoa(j)] = 0
		}

	}

	for i, card := range deck {
		state.hands[i % numPlayers][card] += 1
	}	
}

func sendPlayerCards(gameHub *hub, state *gameState, numPlayers int) {
	for i := 0; i < numPlayers; i++ {
		hand := state.hands[i]
		cardMessage := GameMessage{"player_cards",i,hand}
		sendTo(*gameHub, cardMessage, i)
	}
}

func validPlay(last map[string]int, current map[string]int) bool {
	// TODO: check that player has cards to play.

	assert(len(last) == 1, "last len != 1")	
	assert(len(current) == 1, "current len != 1")
	for currentCard, currentNum := range current {
		for lastCard, lastNum := range last {
			return currentNum == lastNum && currentCard < lastCard
		}
	}
	assert(false, "fell through validPlay")
	return false
}

func playCards(gameHub *hub, state *gameState, incoming GameMessage) {
	state.last = incoming.Cards
	incoming.Message = "played"
	sendToAll(*gameHub, incoming)
}

func incomingCards(gameHub *hub, state *gameState, incoming GameMessage) {
	if state.currentPlayer != incoming.Player {
		// TODO: handle wrong player.
	}
	if len(state.last) == 0 {
		// TODO: handle first play. Can always play.
	} else if validPlay(state.last, incoming.Cards) {
		playCards(gameHub, state, incoming)
	} else {
		// TODO: handle bogus play.
	}
	return
}

func gameLoop(gameHub *hub, state *gameState, numPlayers int) {
	startMessage := GameMessage{"start_game",0,map[string]int{}}
	sendToAll(*gameHub, startMessage)
	for {
		select {}
	}
}

func (all *hub) run() {
	numPlayers := 0
	for {
		select {
		case c := <-all.register:
			all.connections = append(all.connections, c)
			numPlayers++
			if numPlayers == 2 {
				go func() {all.ready <- true;}() // This seems bad.
			}
		case <-all.unregister:
			// TODO: handle unregister.
			// if _, ok := all.connections[c]; ok {
			// 	// delete(all.connections, c)
			// 	// TODO: delete connection somehow.
			// 	close(c.send)
			// }
		case <-all.ready:
			deck := makeDeck()
			shuffledDeck := shuffleDeck(deck)
			dealDeck(&globalState, shuffledDeck, numPlayers)
			
			sendPlayerCards(all, &globalState, numPlayers)
			
			go gameLoop(all, &globalState, numPlayers)
		case <-all.broadcast:
			m := GameMessage{"echo",0,map[string]int{}}
			sendToAll(*all, m)
		case incoming := <-all.process:
			// TODO: need to figure out which player the
			// message is from.
			fmt.Println(incoming)
			var incomingMessage GameMessage
			err := json.Unmarshal(incoming.Message, &incomingMessage)
			if err != nil {
				// TODO: log this
				fmt.Println(err)
				fmt.Println(incoming)
				fmt.Println(incomingMessage)
			}
			incomingMessage.Player = incoming.Player
			incomingCards(all, &globalState, incomingMessage)

		}
		
	}
}
