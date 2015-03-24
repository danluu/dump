package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func charDigit(prev int, char int32) (int, string) {
	diff := char - 'a'
	if char >= 's' {
		diff--
	}

	if char >= 'z' {
		diff--
	}

	digit := int((diff / 3) + 2)
	reps := int((diff % 3) + 1)

	base := ""
	if char == ' ' {
		digit = 0
		reps = 1
	}

	if prev == digit {
		base = " "
	}

	if char == 'z' || char == 's' {
		reps = 4
	}

	resChar := strconv.Itoa(digit)
	res := base + strings.Repeat(resChar, reps)
	return digit, res

}

func main() {
	fname := os.Args[1]
	fd, err := os.Open(fname)
	if err != nil {
		log.Fatal("Failed to open", fname, err)
	}

	scanner := bufio.NewScanner(fd)
	scanner.Scan() // numCases

	iter := 1
	prev := -1
	for scanner.Scan() {
		line := scanner.Text()
		var buf bytes.Buffer
		for _, c := range line {
			var res string
			prev, res = charDigit(prev, c)
			buf.WriteString(res)
		}
		fmt.Printf("Case #%d: %s\n", iter, buf.String())
		iter++
	}

}
