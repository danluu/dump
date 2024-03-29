// html-minifier's recursive mode has some quirks.
// This explicitly runs html-minifier only on files that are valid.

package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

// TODO: fix link spacing so that we don't have to use --conservative-collapse.

// With some versions of html-minify, srcPath can't equal dstPath, so we need to
// add a workaround that puts the output somewhere else and then moves it back.
// However, some (most??) versions work fine without the workaround.

var (
	srcDir   = "../dist"
	dstDir   = "../dist"
	baseArgs = "--remove-comments --collapse-whitespace --conservative-collapse --collapse-boolean-attributes --collapse-inline-tag-whitespace --remove-tag-whitespace --remove-attribute-quotes --use-short-doctype --remove-empty-attributes --remove-optional-tags --remove-empty-elements --minify-css"
)

func minifyFun(path string, info os.FileInfo, err error) error {

	if err != nil {
		log.Fatal(err)
		return nil
	}
	if strings.Contains(path, "file-consistency") {
		fmt.Println("Skipping", path)
		return nil
	}
	if strings.Contains(path, "risc-definition") {
		fmt.Println("Skipping", path)
		return nil
	}
	// Table gets mangled.
	if strings.Contains(path, "bad-decisions") {
		fmt.Println("Skipping", path)
		return nil
	}
	// Table gets mangled
	if strings.Contains(path, "filesystem-errors") {
		fmt.Println("Skipping", path)
		return nil
	}
	// anchor tag gets removed
	if strings.Contains(path, "empirical-pl") {
		fmt.Println("Skipping", path)
		return nil
	}
	// minifier dies with parse error
	if strings.Contains(path, "verilog-vs-vhdl") {
		fmt.Println("Skipping", path)
		return nil
	}
	// Table gets mangled.
	if strings.Contains(path, "cli-complexity") {
		fmt.Println("Skipping", path)
		return nil
	}
	// Table gets mangled.
	if strings.Contains(path, "seo-spam") {
		fmt.Println("Skipping", path)
		return nil
	}
	// Can't handle [ / ] in raw HTML?
	if strings.Contains(path, "elon-twitter-texts") {
		fmt.Println("Skipping", path)
		return nil
	}
	// Table gets mangled.
	if strings.Contains(path, "slow-device") {
		fmt.Println("Skipping", path)
		return nil
	}
	// Table gets mangled.
	if strings.Contains(path, "butler-lampson-1999") {
		fmt.Println("Skipping", path)
		return nil
	}
	if strings.HasSuffix(path, ".html") {
		cmd := "html-minifier"
		dstPath := dstDir + strings.TrimPrefix(path, srcDir)
		badTempPath := "/tmp/mini"
		fmt.Println(dstPath)
		curArgs := baseArgs + " -o " + badTempPath + " " + path
		args := strings.Split(curArgs, " ")
		out, err := exec.Command(cmd, args...).CombinedOutput()
		if err != nil {
			log.Fatal("FAIL", path, string(out), err)
		}
		os.Rename(badTempPath, dstPath)
	}

	return nil
}

func main() {
	fmt.Println("minify")
	err := filepath.Walk(srcDir, minifyFun)
	if err != nil {
		log.Fatal(err)
	}
}
