package main

import (
	"testing"
)

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
}
