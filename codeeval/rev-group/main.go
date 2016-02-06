package main

import "fmt"
import "log"
import "bufio"
import "os"
import "strings"
import "strconv"

func revWithinGroup(i int, j int, aa []string) {
	if j >= len(aa) {
		return
	}
	for i < j {
		aa[i], aa[j] = aa[j], aa[i]
		i = i + 1
		j = j - 1
	}
}

func revGroup(line string) {
	semiSplit := strings.Split(line, ";")
	nn, _ := strconv.Atoi(semiSplit[1])
	numSplit := strings.Split(semiSplit[0], ",")
	for i := 0; i < len(numSplit); i += nn {
		revWithinGroup(i, i+nn-1, numSplit)
	}
	fmt.Println(strings.Join(numSplit, ","))
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		revGroup(scanner.Text())
	}
}
