package main

import (
	"fmt"
	"math"
)

// DP. State of table is mask of which bits are set.
// Value in table is cheapest way to get to have those bits set.
func solve(dist [][]float64, table []float64, nIn int, mask int) float64 {
	if mask == 0 {
		return 0
	}
	if table[mask] >= 0 {
		return table[mask]
	}

	cost := math.Inf(1)
	for i := 0; i < nIn; i++ {
		bitI := 1 << uint(i)
		if mask&bitI > 0 {
			for j := i + 1; j < nIn; j++ {
				bitJ := 1 << uint(j)
				if mask&bitJ > 0 {
					newMask := mask & (^bitI) & (^bitJ)
					cur := dist[i][j] + solve(dist, table, nIn, newMask)
					if cost > cur {
						cost = cur
					}
				}
			}
		}
	}
	table[mask] = cost
	return cost
}

func main() {

	c := 1
	for {
		var nPairs int
		fmt.Scanln(&nPairs)
		if nPairs == 0 {
			return
		}
		nIn := 2 * nPairs
		x := make([]float64, nIn)
		y := make([]float64, nIn)
		table := make([]float64, 1<<uint(nIn))
		for i := range table {
			table[i] = math.Inf(-1)
		}
		for i := 0; i < nIn; i++ {
			var junk string
			fmt.Scanln(&junk, &x[i], &y[i])
		}
		dist := make([][]float64, nIn)
		for i := range dist {
			dist[i] = make([]float64, nIn)
			for j := range dist[i] {
				dist[i][j] = math.Sqrt(
					(x[i]-x[j])*(x[i]-x[j]) +
						(y[i]-y[j])*(y[i]-y[j]))
			}
		}
		ans := solve(dist, table, nIn, 1<<uint(nIn)-1)
		fmt.Printf("Case %d: %.2f\n", c, ans)
		c++
	}
}
