package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strconv"
)

// TODO: fix bad case of returning -1 on no id.
func getCurrentId() int {
	files, err := ioutil.ReadDir(".myvcs/")
	if err != nil {
		log.Fatal("Failed to read .myvcs:", err)
	}

	// files is sorted, so we just want the last valid int.
	id := -1
	for _, f := range files {
		fint, err := strconv.Atoi(f.Name())
		if err == nil {
			id = fint
		}
	}

	return id
}

func getNextId() int {
	return getCurrentId() + 1
}

func copyFile(src string, dst string) (err error) {
	srcFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer srcFile.Close()

	dstFile, err := os.Create(dst)
	if err != nil {
		return err
	}

	_, err = io.Copy(dstFile, srcFile)
	if err != nil {
		// TODO: delete file if we created it but couldn't copy it.
		// In fact, if we fail at all inside a copy we should revert everything.
		// This needs a notion of a transaction.
		return err
	}
	srcStat, err := os.Stat(src)
	if err != nil {
		return err
	}
	err = os.Chmod(dst, srcStat.Mode())
	if err != nil {
		return err
	}

	return
}

func copyDir(src string, dst string) (err error) {
	if src == ".myvcs" {
		return
	}

	srcStat, err := os.Stat(src)
	if err != nil {
		return err
	}

	err = os.MkdirAll(dst, srcStat.Mode())
	if err != nil {
		return err
	}

	contents, err := ioutil.ReadDir(src)
	if err != nil {
		return err
	}

	for _, thing := range contents {
		srcThing := filepath.Join(src, thing.Name())
		dstThing := filepath.Join(dst, thing.Name())

		if thing.IsDir() {
			err = copyDir(srcThing, dstThing)
			if err != nil {
				return err
			}
		} else {
			// Must be a file?
			err = copyFile(srcThing, dstThing)
			if err != nil {
				return err
			}
		}
	}
	return
}

func setHead(next int) {
	byteString := []byte(strconv.Itoa(next))
	ioutil.WriteFile(".myvcs/head", byteString, 0666)
}

func getHead() string {
	head, err := ioutil.ReadFile(".myvcs/head")
	if err != nil {
		log.Fatal("Failed to read head:", err)
	}
	return string(head)
}

func commit() {
	// TODO: handle not being at root.
	// Traverse upwards until we find a ".myvcs"
	id := getNextId()
	src := "."
	dst := filepath.Join(".myvcs", strconv.Itoa(id))
	fmt.Println("DEBUG: copying from", src, "to", dst)
	err := copyDir(src, dst)
	if err != nil {
		log.Fatal("Failed to copyDir: ", err)
	}
	setHead(id)

	return
}

func checkout(id string) {
	src := filepath.Join(".myvcs", id)
	dst := "."
	fmt.Println("DEBUG: copying from", src, "to", dst)
	err := copyDir(src, dst)
	if err != nil {
		log.Fatal("Failed to copyDir: ", err)
	}
}

func main() {
	args := os.Args[1:]
	if len(args) == 0 {
		log.Fatal("Need arguments. Try checkout or commit")
	}

	if args[0] == "commit" {
		commit()
	} else if args[0] == "checkout" {
		if len(args) != 2 {
			log.Fatal("Need name for checkout")
		}
		checkout(args[1])
	} else if args[0] == "latest" {
		id := getCurrentId()
		checkout(strconv.Itoa(id))
	} else if args[0] == "current" {
		fmt.Println(getHead())
	} else {
		log.Fatal("Unknown option:", args)
	}
}
