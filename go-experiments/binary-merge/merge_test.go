package main

import (
	"io/ioutil"
	"log"
	"math/rand"
	"os"
	"path"
	"reflect"
	"sort"
	"strconv"
	"strings"
	"testing"
)

// TODO: generate tests that have errors, check that error handling works.

// ----------------- HELPER FNS ------------------------

// TODO: allow other characters?
func genRandomString(length int) string {
	chars := []byte("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	raw := make([]byte, length)
	for i := range raw {
		raw[i] = chars[rand.Intn(len(chars))]
	}
	return string(raw)
}

func genUniqueRandomString(length int, seen map[string]bool) string {
	attempt := genRandomString(length)
	_, ok := seen[attempt]
	if !ok {
		return genRandomString(length)
	}
	seen[attempt] = true
	return attempt
}

// Generate a list of unique strings, ordered.
func genOrderedStrings(num int, uppercase bool) []string {
	seen := make(map[string]bool)
	all := make([]string, num)
	length := 4 // TODO: randomize? Seems uninteretsing except for very long case, though.
	for i := 0; i < num; i++ {
		someStr := genUniqueRandomString(length, seen)
		if uppercase {
			all[i] = strings.ToUpper(someStr)
		} else {
			all[i] = strings.ToLower(someStr)
		}
	}
	sort.Strings(all)
	return all
}

// Given a list of indices, create a non-empty list that's a subset.
func getSubIndices(supIndices []int) []int {
	var subIndices []int
	for _, i := range supIndices {
		if rand.Intn(3) == 0 {
			subIndices = append(subIndices, i)
		}
	}
	if len(subIndices) == 0 {
		subIndices = append(subIndices, supIndices[rand.Intn(len(supIndices))])
	}
	return subIndices
}

// Create a non-empty random list of (unique) indices, each less than
// num
func genIndices(num int) []int {
	var all []int
	for i := 0; i < num; i++ {
		if rand.Intn(3) == 0 {
			all = append(all, i)
		}
	}
	if len(all) == 0 {
		all = append(all, rand.Intn(num))
	}
	return all
}

// Generate some data that's obviously wrong if we use it as part of
// another field.
func genData(length int) []byte {
	data := make([]byte, length)
	for i := range data {
		data[i] = ^byte(0) // 0xFF
	}
	return data
}

// Generate a valid output file and arbitrarily split the data into
// input files. Collisions possible.  Note: this setup can result in
// objects with 0 keys and keys with 0 length data, but not To make
// for easier debugging, object names are upper case, key names are
// lower case.  keys or object names of length 0.
func genFiles(inFilenames []string, outFilename string) {
	// TODO: allow constants to vary?
	numFiles := len(inFilenames)
	numObjects := 16
	maxKeys := 16

	inFds := make([]*os.File, numFiles)
	outfd, err := os.Create(outFilename)
	if err != nil {
		log.Fatal("Failed to create output file:", err)
	}
	defer outfd.Close()

	for i, fname := range inFilenames {
		inFds[i], err = os.Create(fname)
		if err != nil {
			log.Fatal("Failed to create input file:", err)
		}
	}

	keysPerFile := make([]int, numFiles)

	objNames := genOrderedStrings(numObjects, true)
	// for each object name, generate some key names and values,
	// and then write them to the output file and some arbitrary
	// set of input files.
	for _, oName := range objNames {
		numKeys := rand.Intn(maxKeys + 1)
		objIndices := genIndices(numFiles) // select some input files for this object.
		savedOffsets := make([]int64, numObjects)

		// Write object length/name + number of keys to output file.
		writeField(outfd, []byte(oName))
		writeUint64(outfd, uint64(numKeys))

		keyNames := genOrderedStrings(numKeys, false)
		// Write object length/name to appropriate input files.
		for _, i := range objIndices {
			writeField(inFds[i], []byte(oName))
			savedOffsets[i] = getOffset(inFds[i])
			writeUint64(inFds[i], uint64(0)) // numKeys placeholder.
		}

		// For each key, write it to the output file and
		// select a subset of input files that have been
		// tagged with this object to write to.
		for _, keyName := range keyNames {
			data := genData(rand.Intn(16)) // TODO: lengths.
			writeField(outfd, []byte(keyName))
			writeField(outfd, data)

			keyIndices := getSubIndices(objIndices)
			for _, i := range keyIndices {
				writeField(inFds[i], []byte(keyName))
				writeField(inFds[i], data)
				keysPerFile[i]++
			}
		}

		// Update numKeys placeholders.
		for _, i := range objIndices {
			writeUint64At(inFds[i], uint64(keysPerFile[i]), savedOffsets[i])
		}
		for i := range keysPerFile {
			keysPerFile[i] = 0
		}
	}
}

// Assumes file are small enough to fit in memory.
func filesEqual(testFile string, referenceFile string) bool {
	testData, err := ioutil.ReadFile(testFile)
	if err != nil {
		log.Fatal("failed to open testFile:", testFile, err)
	}
	refData, err := ioutil.ReadFile(referenceFile)
	if err != nil {
		log.Fatal("failed to open refFile:", referenceFile, err)
	}
	return reflect.DeepEqual(testData, refData)
}

// ----------------- UNIT TESTS ------------------------

func TestFirstKeys(t *testing.T) {
	bf0 := []BinFile{
		BinFile{nil, "henwen", 2, 2, ""},
		BinFile{nil, "gurgi", 2, 0, "hobbies"},
		BinFile{nil, "henwen", 1, 0, ""},
	}

	ind0 := []int{1}
	ans0 := firstKeys(bf0, ind0)
	if !reflect.DeepEqual(ans0, []int{1}) {
		t.Fatal("firstKeys", bf0, ind0, "actual", ans0, "expected", []int{1})
	}

	bf1 := []BinFile{
		BinFile{nil, "a", 2, 1, "this_one"},
		BinFile{nil, "z", 1, 0, ""},
		BinFile{nil, "a", 1, 1, ""},
	}
	ind1 := []int{0, 2}
	ans1 := firstKeys(bf1, ind1)
	if !reflect.DeepEqual(ans1, []int{0}) {
		t.Fatal("firstKeys", bf1, ind1, "actual", ans1, "expected", []int{0})
	}

	bf2 := []BinFile{
		{nil, "a", 0, 0, ""},
		{nil, "a", 0, 1, "this_one"},
	}
	ind2 := []int{0, 1}
	ans2 := firstKeys(bf2, ind2)
	if !reflect.DeepEqual(ans2, []int{1}) {
		t.Fatal("firstKeys", bf2, ind2, "actual", ans2, "expected", []int{0})
	}
}

func TestFirstObjects(t *testing.T) {
	bf0 := []BinFile{
		BinFile{nil, "a", 0, 0, ""},
		BinFile{nil, "", 0, 0, ""},
	}
	ans0 := firstObjects(bf0)
	if !reflect.DeepEqual(ans0, []int{0}) {
		t.Fatal("firstObjects", bf0, "actual", ans0, "expected", []int{0})
	}
}

// ----------------- EXISTING END TO END TESTS ------------------------

func TestPreviousFails(t *testing.T) {
	testDirs := []string{"0", "1", "2"}
	inputFiles := []string{"0", "1", "2"}
	baseDir := "regression"
	for _, dir := range testDirs {
		fullInputPath := make([]string, len(inputFiles))
		for i, filename := range inputFiles {
			fullInputPath[i] = path.Join(baseDir, dir, filename)
		}
		outFilename := path.Join(baseDir, dir, "test-out")
		refFilename := path.Join(baseDir, dir, "ref-out")

		mergeFiles(fullInputPath, outFilename)
		if !filesEqual(outFilename, refFilename) {
			t.Fatal("Regression fail", outFilename)
		}
	}

}

// ----------------- RANDOM END TO END TESTS -------------------------

func TestRandInput(t *testing.T) {
	baseDir := "temp" // This should probably use some kind of tmpfile lib.
	for i := 0; i < 100; i++ {
		os.MkdirAll(path.Join(baseDir, strconv.Itoa(i)), 0777)

		numFiles := 3
		inFilenames := make([]string, numFiles)
		for j := range inFilenames {
			inFilenames[j] = path.Join("temp/", strconv.Itoa(i), "/", strconv.Itoa(j))
		}
		outFilename := path.Join("temp/", strconv.Itoa(i), "/test-out")
		refFilename := path.Join("temp/", strconv.Itoa(i), "/ref-out")

		genFiles(inFilenames, refFilename)
		mergeFiles(inFilenames, outFilename)
		if !filesEqual(outFilename, refFilename) {
			t.Fatal("Generated test fail", i, inFilenames, outFilename, refFilename)
		}
	}
}
