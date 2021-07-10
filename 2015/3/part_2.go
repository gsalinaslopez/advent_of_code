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
    robo_x, robo_y := 0, 0
    robo_flag := false
    houses_map := make(map[string]bool)
    houses_map["0,0"] = true
    var coord_string string = ""
    count := 1
    for _, r := range input_line {
        c := string(r)
        if c == "^" {
            if !robo_flag {
                y += 1
            } else {
                robo_y += 1
            }
        }
        if c == ">" {
            if !robo_flag {
                x += 1
            } else {
                robo_x += 1
            }
        }
        if c == "v" {
            if !robo_flag {
                y -= 1
            } else {
                robo_y -= 1
            }
        }
        if c == "<" {
            if !robo_flag {
                x -= 1
            } else {
                robo_x -= 1
            }
        }
        if !robo_flag {
            coord_string = strconv.Itoa(x) + "," + strconv.Itoa(y)
        } else {
            coord_string = strconv.Itoa(robo_x) + "," + strconv.Itoa(robo_y)
        }
        _, contains_key := houses_map[coord_string]
        if !contains_key {
            count += 1
            houses_map[coord_string] = true
        }
        robo_flag = !robo_flag
    }
    fmt.Println(count)
}
