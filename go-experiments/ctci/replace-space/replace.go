package replace

import (
	"bytes"
	"strings"
)

func replaceSpace(sin string) string {
	return strings.Replace(sin, " ", "%20", -1)
}

func replaceSpaceRawSlow(sin string) (res string) {
	for _, char := range sin {
		if char == ' ' {
			res += "%20"
		} else {
			res += string(char)
		}
	}
	return
}

func replaceSpaceRawMid(sin string) string {
	var buf bytes.Buffer
	for _, char := range sin {
		if char == ' ' {
			buf.WriteString("%20")
		} else {
			buf.WriteRune(char)
		}
	}
	return buf.String()
}
