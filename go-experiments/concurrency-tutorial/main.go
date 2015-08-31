package main

import (
	"fmt"
)

func gen(nums ...int) <-chan int {
	out := make(chan int)
	go func() {
		for _, i := range nums {
			out <- i
		}
		close(out)
	}()
	return out
}

func square(in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		for x := range in {
			out <- x * x
		}
		close(out)
	}()
	return out
}

func main() {
	fmt.Println("Concurrency?")
	ch := gen(2, 3, 4, 5)
	sq := square(ch)
	for res := range sq {
		fmt.Println(res)
	}
}
