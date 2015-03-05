package main

import (
	"fmt"
	"math/rand"
)

// randInt64 returns a random integer taking half the range of an int64.
func randInt64(rand *rand.Rand) int64 { return rand.Int63() - 1<<62 }

func dut(a []int) int {
	if len(a) != 4 {
		return 1
	}

	if a[0] > 1<<62 {
		if a[1] > 1<<62 {
			if a[2] > 1<<62 {
				if a[3] > 1<<62 {
					return 0
				}
				return 2
			}
			return 3
		}
		return 4
	}
	return 5
}

func main() {
	var x int
	fmt.Println(x)
}
