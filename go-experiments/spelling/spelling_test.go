package main

import (
	"testing"
)

// TODO: test this more.
func TestSplit(t *testing.T) {
	result := splits("wat")
	if len(result) != 4 {
		t.Error("Bad result from splits(wat)", result)
	}
}
