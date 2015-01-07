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
	lastCards map[string]int
	lastPlayed int
	numPlayers int
	started bool
}

var globalState = gameState{
	currentPlayer: 0,
	firstPass: -1,
	hands: make([]map[string]int, 10), // TODO: fix this 10
	lastCards: make(map[string]int),
	lastPlayed: -1,
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

func playMatchesLast(lastCards map[string]int, current map[string]int) bool {
	// TODO: check that player has cards to play.

	assert(len(lastCards) == 1, "last len != 1")	
	assert(len(current) == 1, "current len != 1")
	for currentCard, currentNum := range current {
		for lastCard, lastNum := range lastCards {
			return currentNum == lastNum && currentCard < lastCard
		}
	}
	assert(false, "fell through playMatchesLast")
	return false
}

func hasCards(hand map[string]int, play map[string]int) bool {
	possiblePlay := true
	for playCard, playNum := range play {
		if handNum, ok := hand[playCard]; ok {
			if (playNum > handNum) {
				possiblePlay = false
			}
		} else {
			possiblePlay = false
		}
	}
	return possiblePlay
}

func validPlay(state *gameState, play GameMessage) bool {
	playerHand := state.hands[play.Player]
	playedCards := play.Cards
	lastCards := state.lastCards
	return playMatchesLast(lastCards, playedCards) && hasCards(playerHand, playedCards)
}

func numCards(set map[string]int) int {
	assert(len(set) == 1, "numCards len(set) != 1")
	for _, numCards := range set { return numCards }
	assert(false, "numCards fallthrough")
	return -1
}

func playCards(gameHub *hub, state *gameState, incoming GameMessage) {
	fmt.Println("playCards")
	fmt.Println(incoming)
	// TODO: subtract played cards from hand.
	// TODO: check for win/exit.
	state.lastCards = incoming.Cards
	state.currentPlayer = state.currentPlayer + 1 % state.numPlayers
	incoming.Message = "played"
	sendToAll(*gameHub, incoming)
}

func passedTurn(gameHub *hub, state *gameState, incoming GameMessage) {
	fmt.Println("passedTurn")
	fmt.Println(incoming)
	if (state.firstPass == -1) {
		state.firstPass = incoming.Player
	} else if (state.firstPass == incoming.Player) {
		// Everybody passed. Hand over.
		if (state.lastPlayed == -1) {
			// Nobody played.
			state.currentPlayer = state.firstPass
			state.firstPass = -1
			state.lastPlayed = -1
			// TODO: send everybody passed message.
		} else {
			// Normal winner
			state.currentPlayer = state.lastPlayed
			state.firstPass = -1
			state.lastPlayed = -1
			// TODO: send hand won message.
		}
	} else {
		// TODO: send pass message.
	}
}

func incomingCards(gameHub *hub, state *gameState, incoming GameMessage) {
	fmt.Println("incomingCards")
	fmt.Println(incoming)
	fmt.Println(state)
	if state.currentPlayer != incoming.Player {
		// TODO: send message indicating wrong player attempted to play.
		return
	}
	if numCards(incoming.Cards) == 0 {
		// Pass.
		passedTurn(gameHub, state, incoming)
	} else if len(state.lastCards) == 0 {
		// First play.
		playCards(gameHub, state, incoming)
	} else if validPlay(state, incoming) {
		// Nth play.
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
