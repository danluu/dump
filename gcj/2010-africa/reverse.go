package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
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

	iter := 1
	for scanner.Scan() {
		line := scanner.Text()
		spline := strings.Split(line, " ")
		var buf bytes.Buffer
		for i := len(spline) - 1; i >= 0; i-- {
			buf.WriteString(spline[i])
			if i > 0 {
				buf.WriteString(" ")
			}
		}
		fmt.Printf("Case #%d: %s\n", iter, buf.String())
		iter++
	}

}
