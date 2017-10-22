package main

import (
	"testing"
)

func main() {

}

func slow(n int) int {
	var sum int
	for i := 0; i < n; i++ {
		x := i + i
		sum += x - i
	}
	return sum
}

func fast(n int) int {
	var sum int
	var x int
	for i := 0; i < n; i++ {
		x = i + i
		sum += x - i
	}
	return sum
}

func BenchmarkInLoop(b *testing.B) {
	slow(b.N)
}

func BenchmarkOutLoop(b *testing.B) {
	fast(b.N)
}
