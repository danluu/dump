package main

import (
	"fmt"
	"strings"
)

func match(pat []string, s string) bool {
	seen := make(map[string]string)

	matchee := strings.Split(s, " ")
	if len(pat) != len(matchee) {
		return false
	}

	for i := 0; i < len(pat); i++ {
		matchWord, ok := seen[pat[i]]
		if !ok {
			seen[pat[i]] = matchee[i]
		} else {
			if matchWord != matchee[i] {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Println(match([]string{"a", "b", "b", "a"}, "cat dog dog cat"))
	fmt.Println(match([]string{"a", "b", "b", "a"}, "cat cat cat cat"))
	fmt.Println(match([]string{"a", "b", "b", "a"}, "cat dog dog dog"))
	fmt.Println(match([]string{"a", "b", "b", "a"}, "cat cat cat dog"))
}
