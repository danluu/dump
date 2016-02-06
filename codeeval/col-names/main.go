package main

import "fmt"
import "log"
import "bufio"
import "os"

// import "strings"
import "strconv"

func digitToStr(x int) string {
	return string('A' + x)
}

func getName(colStr string) {
	col, _ := strconv.Atoi(colStr)
	col--
	res := ""
	for col >= 0 {
		res = digitToStr(col%26) + res
		col = col / 26
		col--
	}
	fmt.Println(res)
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		getName(scanner.Text())
	}
}
