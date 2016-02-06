package main

import "fmt"
import "log"
import "bufio"
import "os"
import "strconv"

func reverse(ss string) string {
	// Warning: doesn't work with unicode.
	runes := []rune(ss)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func addRev(num string) {
	digs, _ := strconv.Atoi(num)
	for i := 0; i < 100; i++ {
		num = strconv.Itoa(digs)
		rev := reverse(num)
		if num == rev {
			fmt.Println(i, rev)
			return
		}
		revDigs, _ := strconv.Atoi(rev)
		digs = digs + revDigs
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
		addRev(scanner.Text())
	}
}
