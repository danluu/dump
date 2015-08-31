package main

import (
	"fmt"
	"sync"
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

func square(done <-chan struct{}, in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for x := range in {
			select {
			case out <- x * x:
			case <-done:
				return
			}
		}
	}()
	return out
}

func merge(done <-chan struct{}, cs ...<-chan int) <-chan int {
	var wg sync.WaitGroup
	out := make(chan int)
	output := func(ch <-chan int) {
		defer wg.Done()
		for x := range ch {
			select {
			case out <- x:
			case <-done:
				return
			}
		}
		wg.Done()
	}

	wg.Add(len(cs))
	for _, ch := range cs {
		go output(ch)
	}

	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

func main() {
	fmt.Println("Concurrency?")
	done := make(chan struct{})
	defer close(done)

	fmt.Println("Part 2")
	nums := gen(2, 3, 5, 7, 11, 13)
	s1 := square(done, nums)
	s2 := square(done, nums)

	out := merge(done, s1, s2)
	fmt.Println(<-out)
	/*
		for res := range merge(done, s1, s2) {
			fmt.Println(res)
		}
	*/

}
