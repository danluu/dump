package main

import (
	"crypto/md5"
	"errors"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"sort"
	"sync"
)

type result struct {
	path string
	sum  [md5.Size]byte
	err  error
}

func sumFiles(done <-chan struct{}, root string) (<-chan result, <-chan error) {
	out := make(chan result)
	errc := make(chan error, 1)
	go func() {
		var wg sync.WaitGroup
		err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if !info.Mode().IsRegular() {
				return nil
			}
			wg.Add(1)
			go func() {
				data, err := ioutil.ReadFile(path)
				select {
				case out <- result{path, md5.Sum(data), err}:
				case <-done:
				}
				wg.Done()
			}()
			select {
			case <-done:
				return errors.New("Walk canceled")
			default:
				return nil
			}
		})
		go func() {
			wg.Wait()
			close(out)
		}()
		errc <- err
	}()
	return out, errc
}

func Md5All(root string) (map[string][md5.Size]byte, error) {
	done := make(chan struct{})
	defer close(done)

	ch, errc := sumFiles(done, root)

	hashes := make(map[string][md5.Size]byte)

	for res := range ch {
		if res.err != nil {
			return nil, res.err
		}
		hashes[res.path] = res.sum
	}
	if err := <-errc; err != nil {
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
