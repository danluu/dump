package main

import (
	"fmt"
)

type pair struct {
	first, second string
}

var (
	alphabet = "abcdefghijklmnopqrstuvwxyz"
)

func splits(word string) []pair {
	result := make([]pair, 0)
	for i := 0; i < len(word)+1; i++ {
		p := pair{word[:i], word[i:]}
		result = append(result, p)
	}
	return result
}

// Note: this can produce duplicates.
func deletes(ps []pair) (result []string) {
	for _, p := range ps {
		if len(p.second) > 0 {
			word := p.first + p.second[1:]
			result = append(result, word)
		}
	}
	return
}

func transposes(ps []pair) (result []string) {
	for _, p := range ps {
		if len(p.second) > 1 {
			word := p.first +
				string(p.second[1]) + string(p.second[0]) +
				p.second[2:]
			result = append(result, word)
		}
	}
	return
}

func replaces(ps []pair) (result []string) {
	for _, p := range ps {
		for _, c := range alphabet {
			if len(p.second) > 0 && uint8(c) != p.second[0] {
				word := p.first + string(c) + p.second[1:]
				result = append(result, word)
			}
		}
	}
	return
}

func inserts(ps []pair) (result []string) {
	for _, p := range ps {
		for _, c := range alphabet {
			word := p.first + string(c) + p.second
			result = append(result, word)
		}
	}
	return
}

func edit1(word string) map[string]struct{} {
	edits := make([][]string, 0)
	ps := splits(word)
	edits = append(edits, deletes(ps))
	edits = append(edits, transposes(ps))
	edits = append(edits, replaces(ps))
	edits = append(edits, inserts(ps))

	result := make(map[string]struct{})
	for _, class := range edits {
		for _, word := range class {
			result[word] = struct{}{}
		}
	}

	return result
}

func main() {
	fmt.Println("Spelling")
	fmt.Println(splits("wat"))
	fmt.Println(deletes(splits("wat")))
	fmt.Println(transposes(splits("wat")))
	fmt.Println(replaces(splits("wat")))
	fmt.Println(inserts(splits("wat")))

	fmt.Println(edit1("wat"))
}
