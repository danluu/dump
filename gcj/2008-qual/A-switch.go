package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	fname := os.Args[1]
	fd, err := os.Open(fname)
	if err != nil {
		log.Fatal("Failed to open", fname, err)
	}

	scanner := bufio.NewScanner(fd)
	scanner.Scan() // numCases

	iter := 1
	for scanner.Scan() {
		numEngines, _ := strconv.Atoi(scanner.Text())
		engineMap := make(map[string]int)
		for i := 0; i < numEngines; i++ {
			scanner.Scan()
			engineName := scanner.Text()
			engineMap[engineName] = i
		}
		greedy := make(map[int]int)
		scanner.Scan()
		numSearches, _ := strconv.Atoi(scanner.Text())
		numSwitches := 0
		for i := 0; i < numSearches; i++ {
			scanner.Scan()
			current, ok := engineMap[scanner.Text()]
			if !ok {
				log.Fatal("Engine lookup failed", i, scanner.Text())
			}
			_, ok = greedy[current]
			if !ok {
				greedy[current] = i
			}
			if len(greedy) == len(engineMap) { // TODO: -1? B/c of current engine.
				greedy = make(map[int]int)
				greedy[current] = i
				numSwitches++
			}
		}
		fmt.Printf("Case #%d: %d\n", iter, numSwitches)
		iter++
	}

}
