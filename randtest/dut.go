package dut

// Written this way to get the coverage tool to expand it.
// Coverage tool doesn't currently expand && or ||
func some_filter(x int) bool {
	for i := 0; i < 16; i = i + 1 {
		if !(x&1 == 1) {
			return false
		}
		x >>= 1
	}
	return true
}

func dut(a []int) int {
	if len(a) != 4 {
		return 1
	}

	if some_filter(a[0]) {
		if some_filter(a[1]) {
			if some_filter(a[2]) {
				if some_filter(a[3]) {
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
