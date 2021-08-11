package main

import(
    "bufio"
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        return;
    }

    total := 0
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := string(scanner.Text())
        fmt.Println(line)
        dimensions := strings.Split(line, "x")
        w, _ := strconv.Atoi(dimensions[0])
        h, _ := strconv.Atoi(dimensions[1])
        l, _ := strconv.Atoi(dimensions[2])
        first_min := w
        var second_min int
        if h < first_min {
            second_min = first_min
            first_min = h
        } else {
            second_min = h
        }
        if l <= first_min {
            second_min = first_min
            first_min = l
        } else if l <= second_min {
            second_min = l
        }
        fmt.Println(first_min, second_min)
        total += 2 * second_min + 2 * first_min + w * h * l
    }
    fmt.Println(total)
}
