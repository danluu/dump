package main

import "fmt"
import "log"
import "bufio"
import "os"
import "strings"
import "strconv"

func mthToLast(nums []string) {
	numsLast := len(nums) - 1
	idx, _ := strconv.Atoi(nums[numsLast])
	if idx < len(nums) {
		fmt.Println(nums[numsLast-idx])
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
		mthToLast(numStrs)
	}
}
