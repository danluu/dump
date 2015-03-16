package zero

// Note: this will add redundant values.
func zeroRowCol(arr [][]int) {
	zeroI := make([]int, 0)
	zeroJ := make([]int, 0)
	for i := range arr {
		for j := range arr[i] {
			if arr[i][j] == 0 {
				zeroI = append(zeroI, i)
				zeroJ = append(zeroJ, j)
			}
		}
	}

	for _, i := range zeroI {
		for j := range arr[i] {
			arr[i][j] = 0
		}
	}

	for i := range arr {
		for _, j := range zeroJ {
			arr[i][j] = 0
		}
	}
}
