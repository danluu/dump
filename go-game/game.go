package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"strconv"
	"strings"
)

const (
	maxCard = 3
)

// currentPlayer:
// finishOrder: order in which players went out. [0] is winner.
// hands:       cards each player has.
// inGame:      whether or not player is still playing.
// lastAction:  last action for each player. For client display.
// lastCards:   cards in "center".
// lastPlayed:  last player to play. Used to determine trick winner.
// numPlayers:
// playerPassed: whether or not player has passed.
// started:     whether or not game has started. Currently unused?
type gameState struct {
	currentPlayer int
	finishOrder   []int
	hands         []map[string]int
	inGame        []bool
	lastAction    []string
	lastCards     map[string]int
	lastPlayed    int
	numPlayers    int
	playerPassed  []bool
	started       bool
}

var globalState = gameState{
	currentPlayer: 0,
	finishOrder:   make([]int, 0),
	hands:         make([]map[string]int, 10), // TODO: fix this 10
	inGame:        make([]bool, 10),           // TODO: fix this 10
	lastAction:    make([]string, 10),         // TODO: fix this 10
	lastCards:     make(map[string]int),
	lastPlayed:    -1,
	numPlayers:    0,
	playerPassed:  make([]bool, 10), // TODO: fix this 10
	started:       false,
}

func resetPassState(state *gameState) {
	for i := 0; i < state.numPlayers; i++ {
		state.playerPassed[i] = false
	}
}

func resetLastAction(state *gameState) {
	for i := 0; i < state.numPlayers; i++ {
		if state.inGame[i] {
			state.lastAction[i] = "None"
		} else {
			state.lastAction[i] = "Out"
		}
	}
}

// Create a deck with i copies of card of value i.
func makeDeck() []string {
	deck := make([]string, 0)
	// Put cards into deck to be shuffled.
	for i := 0; i <= maxCard; i++ {
		if i == 0 {
			// TODO: wildcards.
		} else {
			// Deal out i cards of value i
			for j := 0; j < i; j++ {
				deck = append(deck, strconv.Itoa(i))
			}
		}

	}
	return deck
}

// Shuffle an array. TODO: random seeds.
func shuffleDeck(deck []string) []string {
	shuffledDeck := make([]string, len(deck))
	perm := rand.Perm(len(deck))
	for i, v := range perm {
		shuffledDeck[v] = deck[i]
	}
	return shuffledDeck
}

func dealDeck(state *gameState, deck []string, numPlayers int) {
	// Initialize unitialized maps in array of hands.
	// Also set inGame (deal players into game).
	// And set pass state to false for each player.
	resetPassState(state)
	for i := 0; i < numPlayers; i++ {
		state.inGame[i] = true
		state.hands[i] = make(map[string]int)
		resetLastAction(state)
		for j := 0; j < maxCard+1; j++ {
			state.hands[i][strconv.Itoa(j)] = 0
		}

	}

	for i, card := range deck {
		state.hands[i%numPlayers][card] += 1
	}
}

func sendLastAction(gameHub *hub, state *gameState, lastPlayer int) {
	actionMessage := LastActionMessage{"last_action", lastPlayer, state.lastAction}
	sendToAll(*gameHub, actionMessage)
}

func sendOnePlayerCards(gameHub *hub, state *gameState, player int) {
	hand := state.hands[player]
	cardMessage := GameMessage{"player_cards", player, hand}
	sendTo(*gameHub, cardMessage, player)
}

func sendPlayerCards(gameHub *hub, state *gameState, numPlayers int) {
	for i := 0; i < numPlayers; i++ {
		sendOnePlayerCards(gameHub, state, i)
	}
}

// Check that the current play is the same number of cards of some lower value.
func playMatchesLast(lastCards map[string]int, current map[string]int) bool {
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

// Check that a play is a subset of a hand.
func hasCards(hand map[string]int, play map[string]int) bool {
	possiblePlay := true
	for playCard, playNum := range play {
		if handNum, ok := hand[playCard]; ok {
			if playNum > handNum {
				possiblePlay = false
			}
		} else {
			possiblePlay = false
		}
	}
	return possiblePlay
}

// 1. The player must have the cards they want to play
// 2. If the play isn't the first play of the trick, the cards must match
// the previous play and be of lower rank.
func validPlay(state *gameState, play GameMessage, firstPlay bool) bool {
	playerHand := state.hands[play.Player]
	playedCards := play.Cards
	lastCards := state.lastCards
	playMatches := firstPlay || playMatchesLast(lastCards, playedCards)
	return playMatches && hasCards(playerHand, playedCards)
}

func numCards(set map[string]int) int {
	assert(len(set) == 1, "numCards len(set) != 1")
	for _, numCards := range set {
		return numCards
	}
	assert(false, "numCards fallthrough")
	return -1
}

// Take cards out of a player's hand.
// Return indication that hand is now empty.
func subtractCards(state *gameState, play GameMessage) bool {
	fmt.Println("subtractCards")
	p := play.Player
	for playCard, playNum := range play.Cards {
		if handNum, ok := state.hands[p][playCard]; ok {
			assert(handNum >= playNum, "subtractCards on too many cards")
			state.hands[p][playCard] = handNum - playNum
		} else {
			assert(false, "subtractCards on cards that don't exist")
		}
	}

	handEmpty := true
	for _, num := range state.hands[p] {
		if num > 0 {
			handEmpty = false
		}
	}
	return handEmpty
}

// End game when 1 player is left in since they can just play their cards
// in any arbitrary order.
func isGameOver(state *gameState) bool {
	numActivePlayers := state.numPlayers - len(state.finishOrder)
	return numActivePlayers <= 1
}

// Find next player who isn't out.
func setNextPlayer(state *gameState) {
	fmt.Println("setNextPlayer")
	state.currentPlayer = (state.currentPlayer + 1) % state.numPlayers
	if !state.inGame[state.currentPlayer] {
		setNextPlayer(state)
	}
}

// 1. Remove played cards from hand.
// 2. Check for player exit/win.
// 1/2 handled by subtractCards
// 3. Check if game is over.
// 4. Set last played cards.
// 5. Send message telling everyone what was played.
// 6. Update current player.
// 7. Send message to tell new current player about their cards.
// We assume that the game can only end from this function since players can
// only exit by having played cards.
func playCards(gameHub *hub, state *gameState, incoming GameMessage) {
	fmt.Println("playCards")
	fmt.Println(incoming)

	if subtractCards(state, incoming) {
		state.finishOrder = append(state.finishOrder, state.currentPlayer)
		state.inGame[state.currentPlayer] = false
		sendToAll(*gameHub, GameMessage{"player_out", incoming.Player, map[string]int{}})
	}
	state.lastCards = incoming.Cards

	incoming.Message = "played"
	sendToAll(*gameHub, incoming)
	state.lastPlayed = state.currentPlayer

	// TODO: pretty print or something.
	cardsPlayed := strings.TrimPrefix(fmt.Sprintf("%v", incoming.Cards), "map")
	state.lastAction[state.currentPlayer] = "Played " + cardsPlayed
	sendLastAction(gameHub, state, state.currentPlayer)
	sendOnePlayerCards(gameHub, state, state.currentPlayer)
	if isGameOver(state) {
		sendToAll(*gameHub, GameMessage{"game_over", incoming.Player, map[string]int{}})
		// TODO: send order in which players exited.
		return
		// TODO: set up next game with new player "seating".
	}
	resetPassState(state)
	setNextPlayer(state)
}

func everyonePassed(state *gameState) bool {
	allPass := true
	for i := 0; i < state.numPlayers; i++ {
		if (!state.playerPassed[i]) && state.inGame[i] {
			allPass = false
		}
	}
	return allPass
}

// We keep track of everyone who's passed. That's reset on every card play.
// If everyone who's inGame has passed the trick is over. Play goes to the
// last person to have played.
// TODO: handle case where person who's out gets a turn. At the start of their
// turn there should be a check to see if they're in the game. If they're not,
// setNextPlayer should get called.
// If no one's played and everyone passed, setNextPlayer should set the correct
// next player.
func passedTurn(gameHub *hub, state *gameState, incoming GameMessage) {
	fmt.Println("passedTurn")
	fmt.Println(incoming)

	state.playerPassed[incoming.Player] = true
	if everyonePassed(state) {
		resetPassState(state)
		if state.lastPlayed != -1 {
			// Someone won the trick.
			sendToAll(*gameHub, GameMessage{"won_trick", state.lastPlayed, map[string]int{}})
			state.currentPlayer = state.lastPlayed
			resetLastAction(state)
			state.lastAction[state.lastPlayed] = "Won Trick"
			sendLastAction(gameHub, state, state.lastPlayed)
			state.lastPlayed = -1
			state.lastCards = make(map[string]int) // TODO: don't GC and alloc this
		} else {
			// Everyone passed without playing. Trick over.
			sendToAll(*gameHub, GameMessage{"all_pass", 0, map[string]int{}})
			resetLastAction(state)
			sendLastAction(gameHub, state, incoming.Player)
			setNextPlayer(state)
		}
	} else {
		// A player passed. Trick continues.
		state.lastAction[incoming.Player] = "Passed"
		sendLastAction(gameHub, state, incoming.Player)
		sendToAll(*gameHub, GameMessage{"player_pass", incoming.Player, map[string]int{}})
		setNextPlayer(state)
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
	} else if validPlay(state, incoming, len(state.lastCards) == 0) {
		// Nth play.
		playCards(gameHub, state, incoming)
	} else {
		// TODO: handle bogus play.
	}
	return
}

func (all *hub) run() {
	numPlayers := 0
	for {
		select {
		case c := <-all.register:
			all.connections = append(all.connections, c)
			numPlayers++
			if numPlayers == 2 {
				globalState.numPlayers = 2
				go func() { all.ready <- true }() // This seems bad.
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

			startMessage := GameMessage{"start_game", numPlayers, map[string]int{}}
			sendToAll(*all, startMessage)
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
