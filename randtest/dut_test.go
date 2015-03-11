package dut

import (
	//	"fmt"
	"testing"
)

func TestOnce(t *testing.T) {
	if dut([]int{1, 2, 3, 4}) == 0 {
		t.Errorf("Error from 1 2 3 4")
	}
}

func TestOnceB(t *testing.T) {
	if dut([]int{0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF}) == 0 {
		t.Errorf("Error from 1 2 3 4")
	}
}
