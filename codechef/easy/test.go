package main

import (
	"fmt"
)

func main() {
	var x int
	for {
		_, err := fmt.Scanln(&x)
		if err != nil {
			return
		}
		if x == 42 {
			return
		}
		fmt.Println(x)
	}

}
