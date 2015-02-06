package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os/exec"
	"path/filepath"
	"strings"
)

func execCmd(cmd string) {
	fmt.Println(cmd)
	output, err := exec.Command("sh", "-c", cmd).CombinedOutput()
	if err != nil {
		log.Fatal(string(output), err)
	}
	fmt.Println(string(output))
}

func makeBinaries(binaries map[string]bool) {
	buildCmd := "clang++ -std=c++11 "
	for name, _ := range binaries {
		outName := fmt.Sprintf("-o scratch/%s", name)
		inName := fmt.Sprintf("%s.cc", name)
		fullCmd := fmt.Sprintf("%s %s %s", buildCmd, inName, outName)
		execCmd(fullCmd)
	}
}

func main() {
	files, err := ioutil.ReadDir("./test/")
	if err != nil {
		log.Fatal(err)
	}

	binaries := make(map[string]bool)
	inputs := make(map[string][]string)
	for _, f := range files {
		name := f.Name()
		basename := strings.TrimSuffix(name, filepath.Ext(name))
		binaries[basename] = true
		if strings.HasSuffix(name, ".in") {
			inputs[basename] = append(inputs[basename], name)
		}
	}

	makeBinaries(binaries)
}
