package main

import (
	"math/rand"
)

const (
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
