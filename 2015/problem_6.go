package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    file, err := os.Open("problem_6_input.txt")
    if err != nil {
        return;
    }

    lights_array := make([][]int, 1000)
    for i := 0; i < 1000; i++ {
        lights_array[i] = make([]int, 1000)
    }

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        line := string(scanner.Text())

        if strings.Index(line, "on") != -1 {
            split_str := strings.Split(line, " ")

            coord_str := strings.Split(split_str[2], ",")
            x_start, _ := strconv.Atoi(coord_str[0])
            y_start, _ := strconv.Atoi(coord_str[1])

            coord_str = strings.Split(split_str[4], ",")
            x_end, _ := strconv.Atoi(coord_str[0])
            y_end, _ := strconv.Atoi(coord_str[1])

            fmt.Println("on action ", x_start, y_start, x_end, y_end)
            for i := x_start; i <= x_end; i++ {
                for j := y_start; j <= y_end; j++ {
                    lights_array[i][j] = 1
                }
            }
        }
        if strings.Index(line, "off") != -1 {
            split_str := strings.Split(line, " ")

            coord_str := strings.Split(split_str[2], ",")
            x_start, _ := strconv.Atoi(coord_str[0])
            y_start, _ := strconv.Atoi(coord_str[1])

            coord_str = strings.Split(split_str[4], ",")
            x_end, _ := strconv.Atoi(coord_str[0])
            y_end, _ := strconv.Atoi(coord_str[1])

            fmt.Println("off action ", x_start, y_start, x_end, y_end)
            for i := x_start; i <= x_end; i++ {
                for j := y_start; j <= y_end; j++ {
                    lights_array[i][j] = 0
                }
            }
        }
        if strings.Index(line, "toggle") != -1 {
            split_str := strings.Split(line, " ")

            coord_str := strings.Split(split_str[1], ",")
            x_start, _ := strconv.Atoi(coord_str[0])
            y_start, _ := strconv.Atoi(coord_str[1])

            coord_str = strings.Split(split_str[3], ",")
            x_end, _ := strconv.Atoi(coord_str[0])
            y_end, _ := strconv.Atoi(coord_str[1])

            fmt.Println("toggle action ", x_start, y_start, x_end, y_end)
            for i := x_start; i <= x_end; i++ {
                for j := y_start; j <= y_end; j++ {
                    if lights_array[i][j] == 0 {
                        lights_array[i][j] = 1
                    } else {
                        lights_array[i][j] = 0
                    }
                }
            }
        }
    }

    count := 0
    for i := 0; i < 1000; i++ {
        for j := 0; j < 1000; j++ {
            if lights_array[i][j] == 1 {
                count += 1
           }
        }
    }
    fmt.Println(count)
}
