package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fname := os.Args[1]
	fd, err := os.Open(fname)
	if err != nil {
		log.Fatal("Failed to open", fname, err)
	}

	scanner := bufio.NewScanner(fd)
	scanner.Scan() // numCases

	iter := 0
	for scanner.Scan() {
		cstr := scanner.Text()
		credit, _ := strconv.Atoi(cstr)
		scanner.Scan() // numItems
		scanner.Scan()
		pall := scanner.Text()
		pstr := strings.Split(pall, " ")
		prices := make([]int, len(pstr))
		pmap := make(map[int]int) // value to idx map.
		for i, ps := range pstr {
			prices[i], err = strconv.Atoi(ps)
			if err != nil {
				log.Fatal("strconv price fail", ps, err)
			}
			pmap[prices[i]] = i // Should be safe to ignore duplicates
			// as long as we process in order.
		}

		for i, p := range prices {
			target := credit - p
			idx, ok := pmap[target]
			if ok && idx != i {
				fmt.Printf("Case #%d: %d %d\n", iter+1, i+1, idx+1)
				break
			}

		}

		//fmt.Println("credit", credit)
		//fmt.Println("num", numItems)
		//fmt.Println("prices", prices)
		//fmt.Println("prices", pmap)
		iter++
	}

}
