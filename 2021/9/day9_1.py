dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

with open('day9_1.txt') as file:
    lines = file.readlines()
    max_row = len(lines)
    max_col = len(lines[0].strip())
    low_points = []
    for i in range(len(lines)):
        lines[i] = [int(x) for x in lines[i].strip()]
        for j in range(len(lines[i])):
            low_flag = True
            for d in dir:
                row, col = i + d[0], j + d[1]
                if 0 <= row < max_row and 0 <= col < max_col:
                    if int(lines[i][j]) >= int(lines[row][col]):
                        low_flag = False
                        break
            if low_flag:
                low_points.append(lines[i][j])
    print(low_points)
    low_points_risk = [int(x) + 1 for x in low_points]
    print(sum(low_points_risk))