package rectangle

import (
	"fmt"
)

type Rect interface {
	Update(x int, y int, value int)
	Sum(x1 int, x2int, y1 int, y2 int) int
}

type RectQuickUpdate [][]int

func (re *RectQuickUpdate) Update(x int, y int, value int) {
	(*re)[x][y] = value
}

func (re *RectQuickUpdate) Sum(x1 int, y1 int, x2 int, y2 int) int {
	sum := 0
	if x1 < 0 || x2 < 0 || y1 < 0 || y2 < 0 {
		return 0
	}
	for i := x1; i <= x2; i++ {
		for j := y1; j <= y2; j++ {
			sum += (*re)[i][j]
		}
	}
	return sum
}

type RectQuickSum [][]int

func (re *RectQuickSum) Update(x int, y int, value int) {
	xMax := len(*re)
	yMax := len((*re)[0])

	oldVal := (*re)[x][y]
	if x > 0 {
		oldVal -= (*re)[x-1][y]
	}
	if y > 0 {
		oldVal -= (*re)[x][y-1]
	}
	if x > 0 && y > 0 {
		oldVal += (*re)[x-1][y-1]
	}

	diff := value - oldVal
	fmt.Println("oldVal:", oldVal)
	fmt.Println("diff:", diff)

	for i := x; i < xMax; i++ {
		for j := y; j < yMax; j++ {
			(*re)[i][j] += diff
		}

	}
}

func (re *RectQuickSum) Sum(x1 int, y1 int, x2 int, y2 int) int {
	sum := (*re)[x2][y2]
	if x1 > 0 {
		sum -= (*re)[x1-1][y2]
	}
	if y1 > 0 {
		sum -= (*re)[x2][y1-1]
	}
	if x1 > 0 && y1 > 0 {
		sum += (*re)[x1-1][y1-1]
	}

	return sum
}

// TODO: what's the idiomatic way to do this in go?
func make2dArray(x int, y int) [][]int {
	re := make([][]int, y)
	for i := range re {
		re[i] = make([]int, x)
	}
	return re
}

func makeRectQuickUpdate(x int, y int) RectQuickUpdate {
	return make2dArray(x, y)
}

func makeRectQuickSum(x int, y int) RectQuickSum {
	return make2dArray(x, y)
}

func show2dArray(a [][]int) {
	for i := range a {
		for j := range a[i] {
			fmt.Print(a[i][j], " ")
		}
		fmt.Print("\n")
	}
}

func main() {
	fmt.Println("Rectangle!")
	reQuick := makeRectQuickUpdate(5, 5)
	reSlow := makeRectQuickSum(5, 5)
	fmt.Println(reQuick.Sum(0, 0, 4, 4))
	fmt.Println(reSlow.Sum(0, 0, 4, 4))
	reQuick.Update(0, 0, 1)
	reQuick.Update(2, 2, 128)
	reSlow.Update(0, 0, 1)
	reSlow.Update(2, 2, 128)
	fmt.Println("QuickUpdate")
	fmt.Println(reQuick.Sum(0, 0, 4, 4))
	fmt.Println(reQuick.Sum(0, 0, 0, 0))
	fmt.Println(reQuick.Sum(0, 0, 1, 1))
	fmt.Println(reQuick.Sum(2, 2, 4, 4))
	fmt.Println("QuickSum")
	fmt.Println(reSlow.Sum(0, 0, 4, 4))
	fmt.Println(reSlow.Sum(0, 0, 0, 0))
	fmt.Println(reSlow.Sum(0, 0, 1, 1))
	fmt.Println(reSlow.Sum(2, 2, 4, 4))
	fmt.Println("All QuickSum")
	show2dArray(reSlow)
}
