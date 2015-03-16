package count

import (
	"strings"
)

func count(sin string) int {
	splitString := strings.Fields(sin)
	return len(splitString)
}
