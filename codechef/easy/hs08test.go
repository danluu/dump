package main

import (
	"fmt"
	"log"
)

func main() {
	var (
		attempt   int
		available float64
	)
	_, err := fmt.Scanf("%d %f\n", &attempt, &available)
	if err != nil {
		log.Fatal("Bad input: ", err)
	}

	if attempt%5 != 0 || float64(attempt)+0.5 > available {
		fmt.Printf("%.2f\n", available)
	} else {
		fmt.Printf("%.2f\n", available-(float64(attempt)+0.5))
	}
}
