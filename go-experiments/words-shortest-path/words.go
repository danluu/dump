package main

import (
	"bufio"
	"container/list"
	"fmt"
	"log"
	"os"
)

func isDistanceOne(x string, y string) bool {
	delta := 0

	// Strings are same length. Look for strings that are off by only one.
	if len(x) == len(y) {
		for i := range x {
			if x[i] != y[i] {
				delta++
			}
		}
	}

	// Strings differ in length by one.
	if (len(x)+1 == len(y)) || (len(x) == len(y)+1) {
		var short string
		var long string

		if len(x) > len(y) {
			long = x
			short = y
		} else {
			long = y
			short = x
		}

		is := 0
		il := 0
		for is < len(short) && il < len(long) {
			if long[il] == short[is] {
				is++
				il++
			} else {
				delta++
				il++
			}
		}
		if is == len(short) && il == len(long)-1 && delta == 0 {
			delta = 1
		}
	}
	return delta == 1
}

func makeWordGraph() map[string][]string {
	//	path := "/usr/share/dict/words"
	path := "words.txt"
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Golang doesn't handle having multiple scanners to the same file, so we put stuff into a slice.
	// The word dictionary should easily fit in memory so this should be fine.
	allWords := make([]string, 0)
	fromScan := bufio.NewScanner(file)
	for fromScan.Scan() {
		allWords = append(allWords, fromScan.Text())
	}

	wordGraph := make(map[string][]string)
	for i := range allWords {
		for j := range allWords {
			// fmt.Println("from", allWords[i], "to", allWords[j])
			if isDistanceOne(allWords[i], allWords[j]) {
				wordGraph[allWords[i]] = append(wordGraph[allWords[i]], allWords[j])
				// fmt.Println("Distance one:", allWords[i], allWords[j])
			}
		}
	}

	return wordGraph
}

func reconstructPath(reversePath map[string]string, current string, path *[]string) {
	if prev, ok := reversePath[current]; ok {
		reconstructPath(reversePath, prev, path)
		*path = append(*path, current)
	} else {
		*path = append(*path, current)
	}
}

func findShortestPath(wordGraph map[string][]string, from string, to string) []string {
	path := make([]string, 0)
	if _, ok := wordGraph[from]; !ok {
		return path
	}

	seen := make(map[string]bool)
	queue := list.New()
	queue.PushBack(from)
	seen[from] = true
	reversePath := make(map[string]string)
	for queue.Len() != 0 {
		current := queue.Front()
		// fmt.Println("Start iteration. current", current.Value)
		queue.Remove(current)
		if current.Value == to {
			// fmt.Println("Found", to)
			reconstructPath(reversePath, to, &path)
			return path
		}
		for _, next := range wordGraph[current.Value.(string)] {
			if _, ok := seen[next]; !ok {
				fmt.Println("from", current.Value, "to", next)
				seen[next] = true
				reversePath[next] = current.Value.(string)
				queue.PushBack(next)
			}
		}
		// fmt.Println("End iteration. Len", queue.Len())
	}
	return path // TODO: fix.

}

func main() {
	wordGraph := makeWordGraph()
	path := findShortestPath(wordGraph, "1", "33")
	fmt.Println(path)
}
