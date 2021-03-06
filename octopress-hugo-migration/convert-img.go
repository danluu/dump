package main

// Convert Octopress image links to HTML.
// This would be simpler as a set of regexes; here's an alternate approach just to try handwriting a parser.

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path"
	"path/filepath"
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
			if len(cleaned) > 0 && cleaned != "images" {
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
				log.Fatal("Bad open\n", pair, "\n", tls, "\n")
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

func convertFile(fname string, fi os.FileInfo, err error) error {
	if !fi.IsDir() {
		file, err := os.Open(fname)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		dstDir := "/home/dluu/dev/hugo-wat/content/post/"
		dstFile := dstDir + path.Base(fname)
		wFile, err := os.Create(dstFile)

		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			line := scanner.Text()
			if err := scanner.Err(); err != nil {
				log.Fatal(fname, err)
			}
			if isImg.MatchString(line) {
				tls := tokenizeString(line)
				imgP := convertTokens(tls)
				imgTag := fmt.Sprintf("<img src=\"%s\"", imgP.src)
				if imgP.alt != "" {
					imgTag += fmt.Sprintf(" alt=\"%s\"", strings.Trim(imgP.alt, " "))
				}
				if (imgP.height == "") != (imgP.width == "") {
					log.Fatal("Bad height/width", imgP)
				}
				if imgP.height != "" {
					imgTag += fmt.Sprintf(" width=\"%s\" height=\"%s\"", imgP.width, imgP.height)
				}
				imgTag += ">"
				wFile.WriteString(imgTag + "\n")
			} else {
				wFile.WriteString(line + "\n")
			}
		}

		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}
	}
	return nil
}

func main() {
	filepath.Walk("/home/dluu/dev/hugo-wat/tmp/", convertFile)
}
