package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
)

func main() {
    input_line, err := ioutil.ReadFile("problem_3_input.txt")
    if err != nil {
        fmt.Println(err)
        return
    }

    x, y := 0, 0
    houses_map := make(map[string]bool)
    count := 1
    for _, r := range input_line {
        c := string(r)
        if c == "^" {
            y += 1
        }
        if c == ">" {
            x += 1
        }
        if c == "v" {
            y -= 1
        }
        if c == "<" {
            x -= 1
        }
        coord_string := strconv.Itoa(x) + "," + strconv.Itoa(y)
        _, contains_key := houses_map[coord_string]
        if !contains_key {
            count += 1
            houses_map[coord_string] = true
        }
    }
    fmt.Println(count)
}
