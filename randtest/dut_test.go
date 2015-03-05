package dut

import (
	"testing"
)

func TestOnce(t *testing.T) {
	if dut([]int{1, 2, 3, 4}) == 0 {
		t.Errorf("Error from 1 2 3 4")
	}
}
