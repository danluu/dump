package main

import (
	"log"
	"regexp"
	"strconv"
)

// Some letters followed by some digits.
var reMachine = regexp.MustCompile("([a-zA-Z]+)([0-9]+)")

func lowestAvailable(used map[int]bool) int {
	for i := 0; i < len(used); i++ {
		_, ok := used[i]
		if !ok {
			return i
		}
	}
	return len(used)
}

type ServiceTracker struct {
	used map[string]map[int]bool
}

func (tracker *ServiceTracker) Allocate(name string) string {
	_, ok := tracker.used[name]
	if !ok {
		tracker.used[name] = make(map[int]bool)
	}
	newMachine := lowestAvailable(tracker.used[name])
	tracker.used[name][newMachine] = true
	return name + strconv.Itoa(newMachine)
}

func (tracker *ServiceTracker) Deallocate(machine string) {
	match := reMachine.FindAllStringSubmatch(machine, -1)
	if len(match) != 1 || len(match[0]) != 3 {
		// Expect full match plus two capture groups.
		log.Fatal("Unexpected machine name", machine, match)
	}
	service := match[0][1]
	num, _ := strconv.Atoi(match[0][2])
	delete(tracker.used[service], num)
}
