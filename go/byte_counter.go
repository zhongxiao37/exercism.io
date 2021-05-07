package main

import (
	"fmt"
)

type ByteCounter int

func main() {
	x := ByteCounter(1)
	y := ByteCounter(2)
	fmt.Println(x + y)
}
