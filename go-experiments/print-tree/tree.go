package main

import (
	"strconv"
)

type Tree struct {
	left  *Tree
	val   int
	right *Tree
}

type Wat struct {
	next  *Tree
	level int
}

func makeWat(ptr *Tree, level int) Wat {
	return Wat{ptr, level}
}

func (t *Tree) String() string {
	str := ""

	str += strconv.Itoa(t.val)
	ch := make(chan Wat, 128)
	if t.left != nil {
		ch <- makeWat(t.left, 1)
	}
	if t.right != nil {
		ch <- makeWat(t.right, 1)
	}
	lastLevel := 0
	for len(ch) > 0 {
		w := <-ch
		if lastLevel != w.level {
			str += "\n"
			lastLevel = w.level
		}
		str += strconv.Itoa(w.next.val) + " "
		if w.next.left != nil {
			ch <- makeWat(w.next.left, w.level+1)
		}
		if w.next.right != nil {
			ch <- makeWat(w.next.right, w.level+1)
		}
	}

	return str
}
