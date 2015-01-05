package main

import (
	"testing"
)

func Test_makeDeck_1(t *testing.T) {
	deck := makeDeck()
	if (len(deck) != 13 * 12 / 2) {
		t.Error("Incorrect number of cards")
	}
}

func Test_shuffleDeck_1(t *testing.T) {
	deck := makeDeck()
	// Basically check that we don't crash or lose cards.
	shuffledDeck := shuffleDeck(deck)
	if (len(shuffledDeck) != 13 * 12 / 2) {
		t.Error("Incorrect number of cards")
	}	
}
