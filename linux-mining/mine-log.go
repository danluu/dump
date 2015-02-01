// Rewrite of mine-log.jl since the bug workarounds in that ran into
// yet more Julia bugs.

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
)

var (
	emailMatch = regexp.MustCompile("^Author.*<(.*)@.*>")
)

type AuthorWord struct {
	Name, Word string
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

func main() {
	filename := os.Args[1]
	fmt.Println(filename)

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
	authorWords := make(map[AuthorWord]int)
	for scanner.Scan() {
		line := scanner.Text()
		switch {
		case strings.HasPrefix(line, "commit "):
			// Start of new commit. Process old commit here.
			if !isMergeCommit && author != "" {
				for w, _ := range wordInCommit {
					allWords[w]++
					authorWords[AuthorWord{author, w}]++
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

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}
