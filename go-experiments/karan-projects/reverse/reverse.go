package reverse

// Super inefficient.
func Reverse(sin string) (result string) {
	for _, v := range sin {
		result = string(v) + result
	}
	return
}
