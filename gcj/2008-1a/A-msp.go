package main

import (
	"fmt"
	"sort"
)

func main() {
	var nCases int
	fmt.Scanln(&nCases)
	for c := 1; c <= nCases; c++ {
		var vlen int
		fmt.Scanln(&vlen)
		va := make([]int, vlen)
		vb := make([]int, vlen)
		for i := 0; i < vlen; i++ {
			var x int
			fmt.Scan(&x)
			va[i] = x
		}
		for i := 0; i < vlen; i++ {
			var x int
			fmt.Scan(&x)
			vb[i] = x
		}
		sort.Ints(va)
		sort.Sort(sort.Reverse(sort.IntSlice(vb)))

		prod := 0
		for i := 0; i < vlen; i++ {
			prod += va[i] * vb[i]
		}
		fmt.Printf("Case #%d: %d\n", c, prod)
	}
}
