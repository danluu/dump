package main

import (
	"fmt"
)

func fizzBuzz() {
	for i := 0; i <= 100; i++ {
		switch {
		case i%15 == 0:
			fmt.Println("FizzBuzz")
		case i%5 == 0:
			fmt.Println("Buzz")
		case i%3 == 0:
			fmt.Println("Fizz")
		default:
			fmt.Println(i)
		}
	}
}

func main() {
	fizzBuzz()

}
