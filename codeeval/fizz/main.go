package main

import "fmt"
import "log"
import "bufio"
import "os"
import "strings"
import "strconv"

func fizzBuzz(first int, second int, nn int) {
	parts := make([]string, 0)
	for i := 1; i <= nn; i++ {
		if i%first == 0 && i%second == 0 {
			parts = append(parts, "FB")
		} else if i%first == 0 {
			parts = append(parts, "F")
		} else if i%second == 0 {
			parts = append(parts, "B")
		} else {
			parts = append(parts, strconv.Itoa(i))
		}
	}
	fmt.Println(strings.Join(parts, " "))
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
		nums := make([]int, 3)
		for i, ch := range numStrs {
			nums[i], _ = strconv.Atoi(ch)
		}
		fizzBuzz(nums[0], nums[1], nums[2])
	}
}
