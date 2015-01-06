package main

import (
	"math/rand"
)

const (
	maxCard = 12
)

// last is the last thing played, which needs to get sent to clients
// might not need/want it as part of state.
type gameState struct {
	hands []map[int]int
	last []int
	numPlayers int
	started bool
}

var globalState = gameState{
	hands: make([]map[int]int, 10), // TODO: fix this 10
	last: make([]int,0),
	numPlayers: 0,
	started: false,

}

func makeDeck() []int {
	deck := make([]int, 0)
	// Put cards into deck to be shuffled.
	for i := 0; i <= maxCard; i++ {
		if (i == 0) { 
			// TODO: wildcards.
		} else {
			// Deal out i cards of value i
			for j := 0; j < i; j++ {
				deck = append(deck, i);
			}
		}
		
	}
	return deck
}

func shuffleDeck(deck []int) []int {
	shuffledDeck := make([]int, len(deck))
	perm := rand.Perm(len(deck))
	for i, v := range perm { shuffledDeck[v] = deck[i] }
	return shuffledDeck
}

func dealDeck(state *gameState, deck[]int, numPlayers int) {
	// Initialize unitialized maps in array of hands.
	for i := 0; i < numPlayers; i++ {
		state.hands[i] = make(map[int]int)
		for j := 0; j < maxCard+1; j++ {
			state.hands[i][j] = 0
		}

	}

	for i, card := range deck {
		state.hands[i % numPlayers][card] += 1
	}	
}

func sendPlayerCards(gameHub *hub, state *gameState, numPlayers int) {
	for i := 0; i < numPlayers; i++ {
		cardMessage := GameMessage{"player_cards",i,[]string{}}
		sendTo(*gameHub, cardMessage, i)
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

			startMessage := GameMessage{"start_game",0,[]string{}}
			sendToAll(*all, startMessage)

		case <-all.broadcast:
			m := GameMessage{"echo",0,[]string{}}
			sendToAll(*all, m)
		}
		
	}
}
