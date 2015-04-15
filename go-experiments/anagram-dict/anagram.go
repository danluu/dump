package main

import (
	"fmt"
	"sort"
)

type runeSlice []rune

func (s runeSlice) Len() int {
	return len(s)
}

func (s runeSlice) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s runeSlice) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func countAnagrams(dict []string) int {
	anagram := make(map[string]struct{})
	for _, word := range dict {
		r := []rune(word)
		sort.Sort(runeSlice(r))
		anagram[string(r)] = struct{}{}
	}
	return len(anagram)
}

func main() {
	fmt.Println(countAnagrams([]string{"woo", "oow"}))
	fmt.Println(countAnagrams([]string{"woo", "oow", "ooow"}))
	// TODO: add real tests.
}
