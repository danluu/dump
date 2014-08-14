package main

import "fmt"
import "math"

func main() {
     fmt.Println("Hello, playground")
     fmt.Println(math.Min(1.0, math.NaN()))
     fmt.Println(math.Min(math.NaN(), 1.0))
}
