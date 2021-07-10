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
    current_char := 0
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := string(scanner.Text())
        for _, l := range line {
            c := string(l)
            current_char += 1
            if c == "(" {
                current_floor += 1
            } else {
                current_floor -= 1
            }

            if current_floor < 0 {
                fmt.Println(current_char)
                return
            }
        }
    }
    fmt.Println(current_floor)
}
