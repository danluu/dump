package main

import (
	"log"
)

func fuzzy(fst string, snd string) bool {
	i := 0
	j := 0
	for i < len(fst) && j < len(snd) {
		if fst[i] == snd[j] {
			i++
			j++
		} else {
			j++
		}
	}
	if i == len(fst) && j <= len(snd) {
		return true
	}
	return false
}

func assert(s string, b bool) {
	if !b {
		log.Fatal(s);
	}
}

func main() {
	assert("empty/empty", fuzzy("", ""))
	assert("something/empty", !fuzzy("a", ""))
	assert("empty/something", fuzzy("", "a"))
	assert("self", fuzzy("a", "a"))
	assert("subset left", fuzzy("a", "ab"))
	assert("subset right", fuzzy("b", "ab"))
	assert("subset left over", !fuzzy("aa", "ab"))
	assert("subset right over", !fuzzy("bb", "ab"))
}
