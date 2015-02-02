// Rewrite of mine-log.jl since the bug workarounds in that ran into
// yet more Julia bugs.

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"sort"
	"strings"
)

var (
	emailMatch = regexp.MustCompile("^Author.*<(.*)@.*>")
)

type Pair struct {
	Key string
	Val int
}

type PairVector []Pair

func (p PairVector) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p PairVector) Less(i, j int) bool { return p[i].Val > p[j].Val } // Put biggest first.
func (p PairVector) Len() int           { return len(p) }

// TODO: use a treap if this is on the critical path, which it probably won't be.
func sortMapByValue(m map[string]int) PairVector {
	pairs := make(PairVector, len(m))
	i := 0
	for k, v := range m {
		pairs[i] = Pair{k, v}
		i++
	}
	sort.Sort(pairs)
	return pairs
}

// This isn't great since this can combine stuff that shouldn't be combined.
// However, we get a lot of noise if we don't do something like this.
// TODO: do something that generates less noise.
// TODO: fix the speed of this. This repeated string shrinking is probably very slow
func stripPunct(old string) string {
	old = strings.Replace(old, "(", "", -1)
	old = strings.Replace(old, ")", "", -1)
	old = strings.Replace(old, "\\", "", -1)
	old = strings.Replace(old, ".", "", -1)
	old = strings.Replace(old, "\"", "", -1)
	old = strings.Replace(old, "*", "", -1)
	old = strings.Replace(old, "'", "", -1)
	old = strings.Replace(old, "'", "", -1)
	old = strings.Replace(old, "`", "", -1)
	old = strings.Replace(old, "!", "", -1)
	old = strings.Replace(old, ";", "", -1)
	old = strings.Replace(old, ":", "", -1)
	old = strings.Replace(old, "[", "", -1)
	old = strings.Replace(old, "]", "", -1)
	return old
}

func addWord(m map[string]map[string]int, author, word string) {
	mm, ok := m[author]
	if !ok {
		mm = make(map[string]int)
		m[author] = mm
	}
	mm[word]++
}

func main() {
	filename := os.Args[1]

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	author := ""
	isMergeCommit := false
	wordInCommit := make(map[string]bool)
	allWords := make(map[string]int)
	authorWords := make(map[string]map[string]int)
	authorCommits := make(map[string]int)

	// Loop over all lines. "^commit" demarcates a new "chunk". Count number of times an author uses a word at least
	// once in a chunk. Then use tf-idf to sort word usage.
	for scanner.Scan() {
		line := scanner.Text()
		switch {
		case strings.HasPrefix(line, "commit "):
			// Start of new commit. Process old commit here.
			if !isMergeCommit && author != "" {
				authorCommits[author]++
				for w, _ := range wordInCommit {
					allWords[w]++
					addWord(authorWords, author, w)
				}
			}
			// Reset state.
			isMergeCommit = false
			wordInCommit = make(map[string]bool)
		case strings.HasPrefix(line, "Merge:"):
			isMergeCommit = true
		case strings.HasPrefix(line, "Author:"):
			match := emailMatch.FindStringSubmatch(line)
			if len(match) > 1 {
				author = match[1]
			} else {
				author = ""
				// TODO: handle non-standard emails.
				// TODO: handle full email to prevent aliasing.
			}
		case strings.HasPrefix(line, "Date:"):
			// TODO: handle dates.
		case strings.HasPrefix(line, "    Signed-off-by:"):
			// Ignoring sign offs for now. Could do something to see who signs off on what.
		default:
			line = stripPunct(line)
			words := strings.Split(line, " ")
			for _, w := range words {
				if w != "" {
					wordInCommit[w] = true
				}
			}
		}
	}

	authorList := sortMapByValue(authorCommits)
	for _, authorCommitPair := range authorList {
		theirWords := authorWords[authorCommitPair.Key]
		sortedWords := sortMapByValue(theirWords)
		fmt.Print(authorCommitPair.Key)
		// TODO: generate tf-idf and sort by that instead of sorting by raw usage.
		for _, wordPair := range sortedWords {
			fmt.Print(",", wordPair.Key)
		}
		fmt.Print("\n")
		// fmt.Println(pair)

	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
