package main

import (
	"fmt"
	"time"
)

type Counter struct {
	buckets []int
	head    int
	time    time.Time // time @ head
}

func (c *Counter) adjustTime(t time.Time) {
	newHeadTime := t.Truncate(time.Second)
	diff := int(newHeadTime.Sub(c.time).Seconds())
	if diff > 0 {
		for i := 1; i <= diff; i++ {
			c.buckets[(c.head+i)%len(c.buckets)] = 0
		}
		c.head = (c.head + diff) % len(c.buckets)
		c.time = newHeadTime
	}
}

func (c *Counter) Increment() {
	t := time.Now()
	c.adjustTime(t)
	c.buckets[c.head]++
}

func (c *Counter) Count() int {
	t := time.Now()
	c.adjustTime(t)

	sum := 0
	for _, x := range c.buckets {
		sum += x
	}
	sum -= c.buckets[c.head]
	return sum
}

func NewCounter(num int) *Counter {
	b := make([]int, num)
	headTime := time.Now().Truncate(time.Second)
	return &Counter{b, 0, headTime}
}

func main() {
	fmt.Println("Log thingy")
	c := NewCounter(5)
	fmt.Println(c)
	fmt.Println(c.Count())
	c.Increment()
	c.Increment()
	time.Sleep(3 * time.Second)
	c.Increment()
	c.Increment()
	c.Increment()
	fmt.Println(c)
	fmt.Println(c.Count())
	time.Sleep(1 * time.Second)
	fmt.Println(c.Count())
	time.Sleep(1 * time.Second)
	fmt.Println(c.Count())
	time.Sleep(1 * time.Second)
	fmt.Println(c.Count())
	time.Sleep(1 * time.Second)
	fmt.Println(c.Count())
	time.Sleep(1 * time.Second)
	fmt.Println(c.Count())
}
