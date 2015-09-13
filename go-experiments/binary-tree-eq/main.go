package main

import (
	"fmt"
	"log"
	"math/rand"
)

type Tree struct {
	Left  *Tree
	Value int
	Right *Tree
}

func New(k int) *Tree {
	var t *Tree
	for _, v := range rand.Perm(10) {
		t = insert(t, (1+v)*k)
	}
	return t
}

func insert(t *Tree, v int) *Tree {
	switch {
	case t == nil:
		return &Tree{nil, v, nil}
	case v < t.Value:
		t.Left = insert(t.Left, v)
	case v >= t.Value:
		t.Right = insert(t.Right, v)
	default:
		log.Fatal("Unexpected case on insert(%v, %d)", t, v)
	}
	return t
}

func (t *Tree) String() string {
	if t == nil {
		return "()"
	}
	s := ""
	if t.Left != nil {
		s += t.Left.String() + " "
	}
	s += fmt.Sprint(t.Value)
	if t.Right != nil {
		s += " " + t.Right.String()
	}
	return "(" + s + ")"
}

func Walk(t *Tree, ch chan int, top bool) {
	if t.Left != nil {
		Walk(t.Left, ch, false)
	}
	ch <- t.Value
	if t.Right != nil {
		Walk(t.Right, ch, false)
	}
	if top {
		close(ch)
	}
}

func Same(t1, t2 *Tree) bool {
	ch1 := make(chan int)
	ch2 := make(chan int)
	go Walk(t1, ch1, true)
	go Walk(t2, ch2, true)
	for v1 := range ch1 {
		v2, ok := <-ch2
		fmt.Println(v1, " ", v2)
		if !ok || v1 != v2 {
			return false
		}
	}
	_, ok := <-ch2
	if ok {
		return false
	}
	return true
}

func main() {
	fmt.Println("binary")

	t1 := New(10)
	t2 := New(10)
	fmt.Println(Same(t1, t2))
}
