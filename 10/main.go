package main

// screw this its even slower since idk what im doing with go

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func contains(ref [][]int, s []int) bool {
	for _, slice := range ref {
		lenCheck := true
		elemCheck := true
		sort.Ints(slice)
		// fmt.Printf("ref: %v\n", slice)
		// fmt.Printf("  s: %v\n", s)
		if len(slice) != len(s) {
			continue
		}
		for i, v := range slice {
			// fmt.Printf("comparing: %v %v\n", v, s[i])
			if v != s[i] {
				elemCheck = false
			}
		}
		if lenCheck && elemCheck {
			return true
		}
	}
	return false
}

func remove(s []int, i int) []int {
	s[i] = s[len(s)-1]
	return s[:len(s)-1]
}

// Abs returns absolute value of x
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func getNums(infile string) []int {
	data, err := ioutil.ReadFile(infile)
	check(err)
	var numdata []int
	strdata := strings.Split(string(data), "\n")
	for _, v := range strdata {
		if v == "" {
			continue
		}
		x, err := strconv.Atoi(v)
		check(err)
		numdata = append(numdata, x)
	}
	numdata = append([]int{0}, numdata...)
	sort.Ints(numdata)
	numdata = append(numdata, numdata[len(numdata)-1]+3)
	return numdata
}

func main() {
	infile := "test_input2.txt"
	nums := getNums(infile)

	var valid [][]int
	valid = append(valid, nums)

	for true {
		var keepGoing bool
		fmt.Printf("processing: %v\n", len(valid))
		// for _, v := range valid {
		// 	fmt.Println(v)
		// }

		for _, nums := range valid {
			for i := range nums {
				if (i == 0) || (i == len(nums)-1) {
					continue
				}
				if Abs(nums[i-1]-nums[i+1]) <= 3 {
					var l []int
					l = append(l, nums...)
					l = remove(l, i)
					sort.Ints(l)
					if !contains(valid, l) {
						valid = append(valid, l)
					}
					keepGoing = true
				}
			}
		}
		if !keepGoing {
			break
		}
	}
	fmt.Printf("%v\n", len(valid))
}
