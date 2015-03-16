package replace

import (
	"testing"
)

func TestReplace(t *testing.T) {
	cases := []struct {
		in, want string
	}{
		{"Hello, world", "Hello,%20world"},
		{"Hello, 世界", "Hello,%20世界"},
		{"   . ", "%20%20%20.%20"},
	}
	for _, s := range cases {
		actual := replaceSpace(s.in)
		if actual != s.want {
			t.Errorf("replaceSpace(%q) actual %q expected %q", s.in, actual, s.want)
		}

		actual = replaceSpaceRawSlow(s.in)
		if actual != s.want {
			t.Errorf("replaceSpaceSlow(%q) actual %q expected %q", s.in, actual, s.want)
		}

		actual = replaceSpaceRawMid(s.in)
		if actual != s.want {
			t.Errorf("replaceSpaceMid(%q) actual %q expected %q", s.in, actual, s.want)
		}
	}
}
