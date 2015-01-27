package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// Scan/Scanf aren't fast enough, which is why this uses bufio.
// ReadString('\n') with TrimSpace is also too slow.
// This version barely passes and doesn't really leave time for computation.
// Probably need to manually convert bytes to ints to make this work on a real problem.
func main() {
	var (
		n int
		k int
	)
	ans := 0
	_, err := fmt.Scanf("%d %d\n", &n, &k)
	if err != nil {
		log.Fatal("Bad first line: ", err)
	}

	reader := bufio.NewReader(os.Stdin)
	for i := 0; i < n; i++ {
		line, _, _ := reader.ReadLine()
		x, err := strconv.Atoi(string(line))
		if err != nil {
			break
		}
		if x%k == 0 {
			ans += 1
		}
	}
	fmt.Println(ans)
}
