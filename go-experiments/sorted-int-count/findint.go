package main

import (
	"fmt"
)

func assert(b bool, s string) {
	if !b {
		fmt.Println(s)
	}
}

func brutal(a []int, target int) int {
	count := 0
	for _, x := range a {
		if x == target {
			count++
		}
	}
	return count
}

func binary(a []int, target int) int {
	leftIdx, leftFound := binaryHelper(a, target, 0, len(a)-1, true)
	rightIdx, rightFound := binaryHelper(a, target, 0, len(a)-1, false)
	if !leftFound || !rightFound {
		assert(!leftFound && !rightFound, "Only found either left or right")
		return 0
	}
	return rightIdx - leftIdx + 1
}

func binaryHelper(a []int, target int, left int, right int, leanLeft bool) (int, bool) {
	if right-left == 1 {
		if leanLeft {
			if a[left] == target {
				return left, true
			} else {
				return right, a[right] == target
			}
		} else {
			if a[right] == target {
				return right, true
			} else {
				return left, a[left] == target
			}
		}
	}

	mid := (left + right) / 2
	if target == a[mid] {
		if leanLeft {
			return binaryHelper(a, target, left, mid, leanLeft)
		} else {
			return binaryHelper(a, target, mid, right, leanLeft)
		}
	} else if target > a[mid] {
		return binaryHelper(a, target, mid, right, leanLeft)
	} else {
		return binaryHelper(a, target, left, mid, leanLeft)
	}

	fmt.Println("ERROR: reached end of binaryHelper")
	return -1, false
}

func main() {
	fmt.Println("wat")
}
