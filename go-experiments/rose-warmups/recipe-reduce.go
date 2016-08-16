package main

import (
	"fmt"
	"log"
)

type Unit int

const (
	t Unit = iota
	T
	c
	q
)

type Ingredient struct {
	amount float64
	unit Unit
}

func reduce(ingredient Ingredient) Ingredient {
	if ingredient.unit == t && ingredient.amount >= 3.0 {
		ingredient.amount = ingredient.amount / 3.0
		ingredient.unit = T
	}
	if ingredient.unit == T && ingredient.amount >= 16.0 {
		ingredient.amount = ingredient.amount / 16.0
		ingredient.unit = c
	}
	if ingredient.unit == c && ingredient.amount >= 4 {
		ingredient.amount = ingredient.amount / 4.0
		ingredient.unit = q
	}
	return ingredient
}

func mul(multiplier float64, ingredient Ingredient) Ingredient {
	ingredient.amount = ingredient.amount * multiplier
	return ingredient
}

func solve(multiplier float64, ins []Ingredient) []Ingredient {
	for i, _ := range ins {
		ins[i] = mul(multiplier, ins[i])
		ins[i] = reduce(ins[i])
	}
	return ins
}

func assert(s string, b bool) {
	if !b {
		log.Fatal(s);
	}
}

// TODO: float compares are dangerous. This is bad.
func main() {
	assert("no reduce t", reduce(Ingredient{2.9, t}) == Ingredient{2.9, t})
	assert("reduce t to T", reduce(Ingredient{3.0, t}) == Ingredient{1.0, T})
	assert("reduce t to c", reduce(Ingredient{3.0 * 16, t}) == Ingredient{1.0, c})
	assert("reduce t to q", reduce(Ingredient{3.0 * 16 * 4, t}) == Ingredient{1.0, q})


	wat := solve(2.0,[]Ingredient{
		Ingredient{2.0, c},
		Ingredient{8.0, T},
		Ingredient{2.0, t},
	})
	fmt.Println(wat)
}
