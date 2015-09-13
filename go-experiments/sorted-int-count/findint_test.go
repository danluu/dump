package main

import (
	"fmt"
	"testing"
)

func TestSmoke(t *testing.T) {
	a := []int{1, 2, 11}
	for _, x := range a {
		//		fmt.Println("Test", x)
		resBrutal := brutal(a, x)
		if resBrutal != 1 {
			t.Fatal("Fail check for single brutal.")
		}
		resBinary := binary(a, x)
		if resBinary != 1 {
			t.Fatal("Fail check for single binary.")
		}
	}

	b := []int{-10, 3, 40}
	for _, x := range b {
		//		fmt.Println("Test", x)
		resBrutal := brutal(a, x)
		if resBrutal != 0 {
			t.Fatal("Fail check for single brutal.")
		}
		resBinary := binary(a, x)
		if resBinary != 0 {
			t.Fatal("Fail check for single binary.")
		}

		_, foundLeft := binaryHelper(a, x, 0, 2, true)
		if foundLeft {
			t.Fatal("Found left on empty")
		}

		_, foundRight := binaryHelper(a, x, 0, 2, true)
		if foundRight {
			t.Fatal("Found left on empty")
		}
	}
}

func TestStreak(t *testing.T) {
	fmt.Println("Streak")
	a := []int{1, 2, 2, 5, 5, 5, 5, 5}
	for _, x := range a {
		resBrutal := brutal(a, x)
		if resBrutal != x {
			t.Fatal("Fail check for multi brutal.")
		}
		resBinary := binary(a, x)
		if resBinary != x {
			t.Fatal("Fail check for multi binary.")
		}
	}
}

// TODO: generate some random arrays and check that both fns generate the same result.
