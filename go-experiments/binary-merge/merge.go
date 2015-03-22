package main

import (
	"encoding/binary"
	"io"
	"log"
	"os"
)

/*

Usage:
go run merge.go [input files] [output file]

Merges binary files containing sorted input into a single
file. Individual objects can be larger than memory or even virtual
address space, but individual object names, keys, and values cannot.

The general approach here is to have per-file state for each input
file, which keeps track of how far along we are in each input file.
The topmost loop checks each input file and selects files that are
"next". An inner level loop checks each file that's "next" to
determine which key is next among those.

How current limitations could be bypassed:

1. The limit on name and value size could be eliminated by iteratively
reading and writing fields instead of creating a single allocation per
name or value.

2. There are some int/uint64 conversions that could fail. To run this
on a 32-bit machine, those should probably be converted to uint64
everywhere. The conversions happen as a matter of convenience -- go's
len function returns an int, but the binary write functions want uints
with an explicit size. Elimating them would require a bit more
bookkeeping.

On 64-bit machines, this failure mode is theoretical in the near
future on conventional hardware. Running into the problem would
require a field of length > 2^63 (i.e., > 8 exabytes). With a single
fast enterprise SSD, you might get 3 GB/s, which means that the field
would take about 85 years to read.

3. This was written with absolutely no consideration for
performance. There are a lot of allocations that are immediately
thrown away, which could be eliminated without much work.

The more significant change would be to avoid all copying of data
except as required to write the data. I haven't actually tried this,
but I believe a relatively easy way to do this would be to mmap the
input files and allow the OS to handle paging parts in and out
appropriately as we read. Comparsisons could be done with functions
that operate on bytes to avoid allocating strings at all.

Some comments on style/refactoring:

1. I don't really know go, so this is probably not idiomatic go.

2. Using "" as a sentinal value is sort of heinous and should be refactored out.

3. Keeping finished files inside the array and rechecking them for
eof, instead of removing them is a bit silly and that should be
refactored.

4. The current setup with keyName vs. objName causes a lot of almost,
but not quite, duplicated code.

5. The test generation has a bunch of stuff hardcoded that shouldn't
be hardcoded, and the random distributions are arbitrary and not
picked for any particular reason, and there's nothing that causes
corner cases to get targeted. All of that should be changed. A
somewhat related thing is that I'm pretty sure that the test generator
can generate bogus tests, but I haven't dug into it.

I haven't made the refactoring changes above because I spent about
half a day writing this code, plus time on testing, which seems like
an appropriate amount of time for an interview exercise.

*/

// BinFile tracks per-input file state.
type BinFile struct {
	fd      *os.File
	objName string
	numKeys uint64
	curKey  uint64
	keyName string
}

// Get current offset within file.
func getOffset(fd *os.File) int64 {
	offset, err := fd.Seek(0, 1)
	if err != nil {
		log.Fatal("Seek to get offset failed:", err)
	}
	return offset
}

func readUint64(r io.Reader) (res uint64) {
	err := binary.Read(r, binary.BigEndian, &res)
	if err != nil {
		log.Fatal("failed to read uint64:", err)
	}
	return
}

func readString(r io.Reader, length uint64) string {
	data := make([]byte, length)
	err := binary.Read(r, binary.BigEndian, &data)
	if err != nil {
		log.Fatal("failed to read string:", err)
	}
	return string(data)
}

func readBytes(r io.Reader, length uint64) []byte {
	data := make([]byte, length)
	err := binary.Read(r, binary.BigEndian, &data)
	if err != nil {
		log.Fatal("failed to read []byte:", err)
	}
	return data
}

// os.File as writeAt, but there's no binary.WriteAt
func writeUint64At(w *os.File, outu uint64, offset int64) {
	oldOffset := getOffset(w)
	w.Seek(offset, 0)
	err := binary.Write(w, binary.BigEndian, outu)
	if err != nil {
		log.Fatal("failed to write uint64:", err)
	}
	w.Seek(oldOffset, 0)
	return
}

func writeBytes(w io.Writer, data []byte) {
	err := binary.Write(w, binary.BigEndian, data)
	if err != nil {
		log.Fatal("[]byte write failed:", err)
	}
}

func writeField(w io.Writer, outb []byte) {
	writeUint64(w, uint64(len(outb)))
	writeBytes(w, outb)
}

func writeUint64(w io.Writer, outu uint64) {
	err := binary.Write(w, binary.BigEndian, outu)
	if err != nil {
		log.Fatal("failed to write uint64:", err)
	}
	return
}

// Checks for EOF.  bufio has Peek to handle this case, but we're not
// using bufio.
func isEOF(r *os.File) bool {
	temp := make([]byte, 1)
	n, _ := r.Read(temp)
	r.Seek(int64(-n), 1)
	return n == 0
}

// Get list of alphabetically lowest object names.
func firstObjects(files []BinFile) []int {
	var indices []int
	lowest := files[0].objName
	seenGood := false
	for i, f := range files {
		if f.objName != "" {
			if !seenGood || f.objName < lowest {
				lowest = f.objName
				indices = nil
				seenGood = true
			}
			if f.objName == lowest {
				indices = append(indices, i)

			}
		}
	}
	return indices
}

// Check if any input files contain unread objects.
func objsRemain(files []BinFile) bool {
	for i := range files {
		// This check for "" is necessary because getObjName
		// reads numKeys. If the last object is an object with
		// numKeys == 0, we'll be at eof even though we need
		// to write the object.  The check for isEOF is
		// necessary because we don't have a special function
		// to move the state out of "" the first time this is
		// run. This check could be simplified to a single
		// check by changing either of those things above.
		if !(isEOF(files[i].fd) && files[i].objName == "") {
			return true
		}
	}
	return false
}

// Read object frame (length, name, number of keys/vals).
func getObjNames(files []BinFile) {
	for i := range files {
		if files[i].objName == "" && !isEOF(files[i].fd) {
			objNameLen := readUint64(files[i].fd)
			objName := readString(files[i].fd, objNameLen)
			files[i].objName = objName
			numKeys := readUint64(files[i].fd)
			files[i].numKeys = numKeys
		}
	}
}

// Get list of alphabetically lowest key names.  Returning multiple
// values from this indicates that we have a collision.  This nonsense
// with seenGood is to handle the case when we have keys with numKeys
// == 0.
func firstKeys(files []BinFile, indices []int) []int {
	var keyIndices []int
	lowest := ""
	seenGood := false
	for _, i := range indices {
		if files[i].keyName != "" {
			if !seenGood || files[i].keyName < lowest {
				lowest = files[i].keyName
				keyIndices = nil
				seenGood = true
			}
			if files[i].keyName == lowest {
				keyIndices = append(keyIndices, i)
			}
		}
	}
	return keyIndices
}

// Read key lengths and names from input files.
func readKeyNames(files []BinFile, indices []int) {
	for _, i := range indices {
		if files[i].keyName == "" && (files[i].curKey < files[i].numKeys) {
			keyNameLen := readUint64(files[i].fd)
			keyName := readString(files[i].fd, keyNameLen)
			files[i].keyName = keyName
		}
	}
}

// Read value lengths and values from input files.  On collisions,
// arbitrarily use data from "last" file.
func readData(files []BinFile, keyIndices []int) []byte {
	var valLen uint64
	var data []byte
	for _, i := range keyIndices {
		valLen = readUint64(files[i].fd)
		data = readBytes(files[i].fd, valLen)
	}
	return data
}

// Check if relevant input files have unread keys in current object.
func keysRemain(files []BinFile, indices []int) bool {
	for _, i := range indices {
		if files[i].numKeys > files[i].curKey {
			return true
		}
		if files[i].numKeys < files[i].curKey {
			log.Fatal("numKeys < curKey")
		}
	}
	return false
}

func incrementKeys(files []BinFile, keyIndices []int) {
	for _, i := range keyIndices {
		files[i].curKey++
	}
}

func resetKeyNames(files []BinFile, keyIndices []int) {
	for _, i := range keyIndices {
		files[i].keyName = ""
	}
}

func resetObjNames(files []BinFile, indices []int) {
	for _, i := range indices {
		files[i].curKey = 0
		files[i].objName = ""
	}
}

// Write a single object out to output file.  As a side effect,
// advance all input file pointers past the end of that object.
// Basically, write object/length name (already read), then read/write
// keys/values while any "lowest" objects have keys remaining.
func writeObj(files []BinFile, outfd *os.File) {
	indices := firstObjects(files) // indices of alphabetically lowest objects.
	if len(indices) == 0 {
		log.Fatal("objIndices empty", files)
	}

	objName := files[indices[0]].objName
	writeField(outfd, []byte(objName)) // write object length, name.

	offsetNumKeys := getOffset(outfd)
	writeUint64(outfd, 0) // write placeholder for number of keys.

	numKeys := uint64(0)
	for keysRemain(files, indices) {
		readKeyNames(files, indices)
		keyIndices := firstKeys(files, indices) // indices of alphabetically lowest keys.
		if len(keyIndices) == 0 {
			log.Fatal("keyIndices empty", files)
		}
		keyName := files[keyIndices[0]].keyName
		writeField(outfd, []byte(keyName)) // write key length and name.

		data := readData(files, keyIndices)
		writeField(outfd, data) // write value length and conents.

		// Update state to restore invariants.
		resetKeyNames(files, keyIndices)
		incrementKeys(files, keyIndices)
		numKeys++

	}
	writeUint64At(outfd, numKeys, offsetNumKeys)
	resetObjNames(files, indices)
}

func openInputFiles(filenames []string) []BinFile {
	files := make([]BinFile, len(filenames))
	for i, fname := range filenames {
		fd, err := os.Open(fname)
		if err != nil {
			log.Fatal("Failed to open input file ", err)
		}
		files[i].fd = fd
	}
	return files
}

// While any input files have unread objects, find the alphabetically
// lowest object name and write it to the output file.
func mergeFiles(filenames []string, outFilename string) {
	outfd, err := os.Create(outFilename)
	if err != nil {
		log.Fatal("Failed to open output file ", err)
	}
	defer outfd.Close()

	files := openInputFiles(filenames)
	for _, infile := range files {
		defer infile.fd.Close()
	}

	for objsRemain(files) {
		getObjNames(files)
		writeObj(files, outfd)
	}
}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Two or more arguments required. Last argument is output filename. Rest are input filenames")
	}

	filenames := os.Args[1 : len(os.Args)-1] // All but last argument.
	outFilename := os.Args[len(os.Args)-1]   // Last argument.

	mergeFiles(filenames, outFilename)
}
