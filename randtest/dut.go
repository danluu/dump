package dut

func dut(a []int) int {
	if len(a) != 4 {
		return 1
	}

	if a[0] > 1<<62 {
		if a[1] > 1<<62 {
			if a[2] > 1<<62 {
				if a[3] > 1<<62 {
					return 0
				}
				return 2
			}
			return 3
		}
		return 4
	}
	return 5
}
