package main

import "fmt"

func main() {
     var a uint64
     var b int64
     a = 0xffffffffffffffff
     b = -1        
     fmt.Println("%i", b > a);
     fmt.Println("%i", a > b);
     fmt.Println("%i", a == b);
}
