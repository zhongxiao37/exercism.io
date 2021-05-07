

package main

import (
  "fmt"
)

func main() {
  
  q := [...]int{1, 2, 3}
  fmt.Printf("%T\n", q) // "[3]int"
  fmt.Printf("%v\n", q) // "[1,2,3]"
  numbers := []int{1,2}
  numbers = append(numbers, 3, 4)  // [1,2,3,4]
	fmt.Printf("%v\n", numbers) // "[1,2,3,4]"  
}


