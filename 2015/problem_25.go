package main

import (
    "fmt"
)

func gen_next_code(x int) int {
    return (x * 252533) % 33554393
}

func main() {
    row_delim := 0
    row, col := 0, 0

    current_code := 20151125
    for row !=  2980 || col != 3074 {
        // attempt to go diagonally
        if row - 1 < 0 {
            row_delim += 1
            row = row_delim
            col = 0
        } else {
            row -= 1
            col += 1
        }

        current_code = gen_next_code(current_code)
    }
    fmt.Println(current_code)
}
