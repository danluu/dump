package main

import (
	"crypto/md5"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"sort"
)

func Md5All(root string) (map[string][md5.Size]byte, error) {
	hashes := make(map[string][md5.Size]byte)
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.Mode().IsRegular() {
			return nil
		}
		data, err := ioutil.ReadFile(path)
		if err != nil {
			return err
		}
		hashes[path] = md5.Sum(data)
		return nil
	})
	if err != nil {
		return nil, err
	}
	return hashes, nil
}

func main() {
	fmt.Println("md5")
	hashes, err := Md5All(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}
	var paths []string
	for path := range hashes {
		paths = append(paths, path)
	}
	sort.Strings(paths)
	for _, p := range paths {
		fmt.Printf("%x %s\n", hashes[p], p)
	}
}
