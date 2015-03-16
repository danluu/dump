package count

import (
	"testing"
)

func TestSplit(t *testing.T) {
	cases := []struct {
		in   string
		want int
	}{
		{"hoho ho", 2},
		{"wat wat \twat ", 3},
		{"", 0},
		{"one", 1},
		{"Hello, 世界", 2},
	}

	for _, c := range cases {
		res := count(c.in)
		if res != c.want {
			t.Errorf("Actual", res, "Expected", c.want)
		}
	}
}
