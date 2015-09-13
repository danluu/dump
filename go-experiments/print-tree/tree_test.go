package main

import (
	"fmt"
	"testing"
)

func TestSmoke(t *testing.T) {
	fmt.Println("empty test")
	var x Tree
	x.val = 3

	var left Tree
	x.left = &left
	left.val = 2

	var right Tree
	x.right = &right
	right.val = 20

	var rl Tree
	right.left = &rl
	rl.val = 10
	fmt.Println(x.String())
}
