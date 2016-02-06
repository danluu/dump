package main

// Convert Octopress image links to HTML.
// This would be simpler as a set of regexes; here's an alternate approach just to try handwriting a parser.

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var (
	isImg = regexp.MustCompile(`{\s*%\s+img\s`)
)

type Token int

const (
	open Token = iota
	close
	digits
	img
	center
	text
)

type State int

const (
	expectOpen State = iota
	expectImg
	expectURI
	expectDig1OrCaption
	expectDig2
	expectCaption
)

type TokenLit struct {
	t Token
	l string
}

type ImgParts struct {
	src    string
	alt    string
	width  string
	height string
}

// TODO: handle escaping.
// TODO: assert that "{%" is never broken up with a space.
// This was checked seperate but the assert should be built in here.
func tokenizeString(octoString string) []TokenLit {
	res := make([]TokenLit, 0)
	parts := strings.Split(octoString, " ")
	for _, literal := range parts {
		if literal == "{%" {
			res = append(res, TokenLit{open, ""})
		} else if literal == "%}" {
			res = append(res, TokenLit{close, ""})
		} else if literal == "img" {
			res = append(res, TokenLit{img, literal})
		} else if literal == "center" {
			res = append(res, TokenLit{center, literal})
		} else if _, err := strconv.Atoi(literal); err == nil {
			res = append(res, TokenLit{digits, literal})
		} else {
			cleaned := strings.Trim(literal, "'`‘")
			if len(cleaned) > 0 {
				res = append(res, TokenLit{text, cleaned})
			}
		}

	}
	return res
}

func convertTokens(tls []TokenLit) ImgParts {
	res := ImgParts{"", "", "", ""}
	state := expectOpen
	for _, pair := range tls {
		switch state {
		case expectOpen:
			if pair.t != open {
				log.Fatal("Bad open", pair, tls)
			}
			state = expectImg

		case expectImg:
			if pair.t != img {
				log.Fatal("Bad img", pair, tls)
			}
			state = expectURI
		case expectURI:
			if pair.t == center {
				continue
			} else if pair.t != text {
				log.Fatal("Bad URI", pair, tls)
			}
			res.src = pair.l
			state = expectDig1OrCaption
		case expectDig1OrCaption:
			if pair.t == digits {
				// TODO: this will break if text starts with digits.
				res.width = pair.l
				state = expectDig2
			} else if pair.t == text {
				// TODO: handle case where text is img or center.
				res.alt += pair.l
				state = expectCaption
			} else if pair.t == close {
				// TODO: assert that we're done with tls.
				return res
			}
		case expectDig2:
			if pair.t != digits {
				log.Fatal("Unexpected non-digits", pair, tls)
			}
			res.height = pair.l
			state = expectCaption
		case expectCaption:
			if pair.t == text {
				// TODO: handle case where text is img or center.
				res.alt += " " + pair.l
				state = expectCaption
			} else if pair.t == close {
				// TODO: assert that we're done with tls.
				return res
			}
		}
	}

	return res
}

func convertFile(fname string) {
	file, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if isImg.MatchString(line) {
			tls := tokenizeString(line)
			fmt.Println(tls)
			imgP := convertTokens(tls)
			fmt.Println(imgP)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

func main() {
	fmt.Println("wat")

	testFile := "/home/dluu/dev/hugo-wat/content/post/2choices-eviction.markdown"
	convertFile(testFile)
}
