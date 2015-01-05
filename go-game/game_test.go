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
