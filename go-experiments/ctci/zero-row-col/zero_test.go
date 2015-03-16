package zero

import (
	"fmt"
	"testing"
)

func SingleZero(arr [][]int, x int, y int) {
	for i := range arr {
		for j := range arr[i] {
			arr[i][j] = 1
		}
	}
	arr[x][y] = 0
}

// TODO: make test actually test something!
func TestZero(t *testing.T) {
	arr := make([][]int, 3)
	for i := range arr {
		arr[i] = make([]int, 3)
	}
	SingleZero(arr, 0, 0)
	zeroRowCol(arr)
	fmt.Println(arr)

	SingleZero(arr, 1, 1)
	zeroRowCol(arr)
	fmt.Println(arr)

	SingleZero(arr, 1, 2)
	zeroRowCol(arr)
	fmt.Println(arr)
}
