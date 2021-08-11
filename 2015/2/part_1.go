
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
        w2 := l * w
        h2 := w * h
        l2 := h * l
        min := w2
        if h2 < min {
          min = h2
        }
        if l2 < min {
          min = l2
        }
        total += 2*w2 + 2*h2 + 2*l2 + min
    }
    fmt.Println(total)
}
