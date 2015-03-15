package main

import (
	"fmt"
)

type Counter int

type Incrementable interface {
	Init()
	Inc()
	PrintValue()
}

func (c *Counter) Init() {
	*c = 0
}

func (c *Counter) Inc() {
	*c++
}

func (c Counter) IncNotReallyInc() {
	c++
}

func (c *Counter) PrintValue() {
	fmt.Println(*c)
}

func incrementSome(i Incrementable) {
	i.Inc()
	i.PrintValue()
	i.Inc()
	i.PrintValue()
}

func main() {
	fmt.Println("Test!")

	var c Counter
	c.Init()
	c.PrintValue()
	c.Inc()
	c.PrintValue()
	incrementSome(&c)
	fmt.Println("Fake Inc")
	c.IncNotReallyInc()
	c.PrintValue()
}
