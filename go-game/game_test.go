package main

import (
	"fmt"
	"testing"
)

// func Test_serializeHand(t *testing.T) {
// 	hand := make(map[int]int)
// 	fmt.Println(hand)
// 	hand[0] = 0
// 	hand[12] = 7
// }

// Check for correct number of cards.
func Test_makeDeck_1(t *testing.T) {
	deck := makeDeck()
	if (len(deck) != 13 * 12 / 2) {
		t.Error("Incorrect number of cards")
	}
}

// Check for correct number of cards after shuffling.
func Test_shuffleDeck_1(t *testing.T) {
	deck := makeDeck()
	shuffledDeck := shuffleDeck(deck)
	if (len(shuffledDeck) != 13 * 12 / 2) {
		t.Error("Incorrect number of cards")
	}	
}

// Check that we can deal out cards without crashing. Unshuffled deck.
func Test_dealDeck_1(t *testing.T) {
	deck := makeDeck()
	numPlayers := 2
	someState := gameState{
		hands: make([]map[int]int, 10),
		last: make([]int,0),
		numPlayers: 0,
		started: false,
	}
	dealDeck(&someState, deck, numPlayers)
	
	p0Cards := someState.hands[0]
	p0Total := 0
	for _, num := range p0Cards {
		p0Total += num
	}
	if (p0Total != 39) {
		fmt.Println(p0Total)
		t.Error("Incorrect number of p0 cards")
	}
}
