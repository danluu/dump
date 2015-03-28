package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

type pair struct {
	time   int
	arrive bool
}

type Pairs []pair

func (x Pairs) Len() int {
	return len(x)
}

func (x Pairs) Swap(i, j int) {
	x[i], x[j] = x[j], x[i]
}

func (x Pairs) Less(i, j int) bool {
	if x[i].time == x[j].time {
		return x[i].arrive
	} else {
		return x[i].time < x[j].time
	}
}

func needed(ps Pairs) int {
	sort.Sort(ps)
	curNeed := 0
	maxNeed := 0
	for _, p := range ps {
		if p.arrive {
			curNeed--
		} else {
			curNeed++
		}
		if curNeed > maxNeed {
			maxNeed = curNeed
		}

	}
	return maxNeed
}

func minutes(s string) int {
	sp := strings.Split(s, ":")
	hour, _ := strconv.Atoi(sp[0])
	minute, _ := strconv.Atoi(sp[1])
	return (hour * 60) + minute
}

func main() {
	var nCases int
	fmt.Scanln(&nCases)

	for c := 1; c <= nCases; c++ {
		var ntr, na, nb int
		var ar, de string
		fmt.Scanln(&ntr)
		fmt.Scanln(&na, &nb)
		aSide := make(Pairs, 0)
		bSide := make(Pairs, 0)
		for i := 0; i < na; i++ {
			fmt.Scanln(&de, &ar)
			depart := minutes(de)
			arrive := minutes(ar) + ntr
			aSide = append(aSide, pair{depart, false})
			bSide = append(bSide, pair{arrive, true})
		}
		for i := 0; i < nb; i++ {
			fmt.Scanln(&de, &ar)
			depart := minutes(de)
			arrive := minutes(ar) + ntr
			aSide = append(aSide, pair{arrive, true})
			bSide = append(bSide, pair{depart, false})
		}
		aNeed := needed(aSide)
		bNeed := needed(bSide)
		fmt.Printf("Case #%d: %d %d\n", c, aNeed, bNeed)
	}
}
