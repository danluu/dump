package main

import (
	"fmt"
	"testing"
)

func TestAvail(t *testing.T) {
	cases := []struct {
		in   map[int]bool
		want int
	}{
		{map[int]bool{0: true, 2: true}, 1},
		{map[int]bool{1: true}, 0},
		{map[int]bool{}, 0},
	}
	for _, c := range cases {
		got := lowestAvailable(c.in)
		if got != c.want {
			t.Errorf("lowestAvailable(%v) == %d, want %d", c.in, got, c.want)
		}
	}

}

func TestAllocDealloc(t *testing.T) {
	// TODO: make test actually test this.
	tracker := &ServiceTracker{make(map[string]map[int]bool)}
	tracker.Allocate("stripe")
	tracker.Allocate("stripe")
	tracker.Allocate("stripe")
	tracker.Allocate("polkadot")
	fmt.Println(tracker)
	tracker.Deallocate("stripe1")
	fmt.Println(tracker)
	tracker.Allocate("stripe")
	fmt.Println(tracker)
}
