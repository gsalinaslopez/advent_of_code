package main

import(
    "bufio"
    "fmt"
    "os"
)

func main() {
    file, err := os.Open("part1_input.txt")
    if err != nil {
        return;
    }

    current_floor := 0
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := string(scanner.Text())
        for _, l := range line {
            c := string(l)
            if c == "(" {
                current_floor += 1
            } else {
                current_floor -= 1
            }
        }
    }
    fmt.Println(current_floor)
}
