package mylist

import (
	"fmt"
	"testing"
)

func TestInsert(t *testing.T) {
	initial := new(Node)
	initial.val = 0
	initial.next = nil

	node1 := initial.Insert(1)
	node2 := node1.Insert(2)
	node1.Insert(12)

	fmt.Println(initial, node1, node1.next, node2)
	// Should have initial->node1->node12->node2.
	if initial.val != 0 {
		t.Errorf("initial.val != 0", initial)
	}
	if initial.next.val != 1 {
		t.Errorf("node1.val != 1 %q", initial)
	}

	if initial.next.next.val != 12 {
		t.Errorf("node12.val != 1 %q", initial)
	}

	if initial.next.next.next.val != 2 {
		t.Errorf("node12.val != 2 %q", initial)
	}
}
