package main

import "fmt"
import "log"
import "bufio"
import "os"
import "strings"

func detectCycle(nums []string) {
	gg := make(map[string]int)
	res := make([]string, 0)

	for _, cur := range nums {
		if gg[cur] > 1 {
			fmt.Println(strings.Join(res, " "))
			return
		} else if gg[cur] == 1 {
			res = append(res, cur)
		}
		gg[cur]++
	}
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		numStrs := strings.Split(scanner.Text(), " ")
		detectCycle(numStrs)
	}
}
