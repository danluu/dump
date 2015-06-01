package main

import (
	"bytes"
	"fmt"
	"strconv"
)

// We use this horrible hack because we can't have a map of []int.
// We could use a built-in go hash function and have a low probability of collision, or convert
// []int to []byte to []string.
// Another possibility would be to use generate and generate a struct of ints of the appropriate length.
func hashCoins(amount int, used []int) string {
	var buf bytes.Buffer
	for _, x := range used {
		buf.WriteString(strconv.Itoa(x) + ",")
	}
	buf.WriteString(strconv.Itoa(amount))

	return buf.String()
}

func change(coins []int, amount int, used []int, results *[][]int, seen map[string]struct{}) {
	hash := hashCoins(amount, used)
	_, ok := seen[hash]
	if ok {
		return
	} else if amount < 0 {
		return
	} else if amount == 0 {
		*results = append(*results, used)
	}

	seen[hash] = struct{}{}

	for i, coinValue := range coins {
		nextUsed := make([]int, len(used))
		copy(nextUsed, used)
		nextUsed[i]++
		change(coins, amount-coinValue, nextUsed, results, seen)
	}
}

func main() {
	fmt.Println("Change")
	results := make([][]int, 0)
	coins := []int{1, 5, 10}
	used := make([]int, len(coins))
	seen := make(map[string]struct{})
	change(coins, 10, used, &results, seen)
	fmt.Println(results)
}
