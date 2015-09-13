package main

import (
	"testing"
)

func TestSmoke(t *testing.T) {
	aab := post2nfa("aab")
	if !match(aab, "aab") {
		t.Fatal("aab didn't match aab")
	}
	nonMatches := []string{"aa", "a", "ab", "", "baab", "bab", "abb"}
	for _, miss := range nonMatches {
		if match(aab, miss) {
			t.Fatal("Bad match against", miss)
		}
	}
}

func TestStar(t *testing.T) {
	aStar := post2nfa("a*")
	aStarHits := []string{"a", "aa", "aaa", "aaaaaaaaaaaaaaaaaaaaaaaa", "", "ab", "aab", "aaab", "aaaaaaaaaaaaaab", "b"}
	for _, hit := range aStarHits {
		if !match(aStar, hit) {
			t.Fatal("Failed match against a*:", hit)
		}
	}

	aStarB := post2nfa("a*b")
	aStarBHits := []string{"ab", "aab", "aaab", "aaaaaaaaaaaaaab", "b"}
	for _, hit := range aStarBHits {
		if !match(aStarB, hit) {
			t.Fatal("Failed match against a*b:", hit)
		}
	}

	aStarBMisses := []string{"a", "aa", "aaa", "aaaaaaaaaaaaaaaaaaaaaaaa", ""}
	for _, miss := range aStarBMisses {
		if match(aStarB, miss) {
			t.Fatal("Failed match against a*b:", miss)
		}
	}

}
