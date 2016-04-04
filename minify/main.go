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

var (
	srcDir   = "/home/dluu/dev/dist"
	dstDir   = "/home/dluu/dev/dist"
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
	if strings.HasSuffix(path, ".html") {
		cmd := "html-minifier"
		dstPath := dstDir + strings.TrimPrefix(path, srcDir)
		fmt.Println(dstPath)
		curArgs := baseArgs + " -o " + dstPath + " " + path
		args := strings.Split(curArgs, " ")
		_, err := exec.Command(cmd, args...).Output()
		if err != nil {
			log.Fatal("FAIL", path, err)
		}
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
