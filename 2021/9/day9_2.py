dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

with open('day9_2.txt') as file:
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
                low_points.append((int(i),int(j)))
    print(low_points)

    def bfs(start):
        ret = 0
        queue = [start]
        visited = {}
        while len(queue) > 0:
            node = queue[0]
            node_str = str(node[0]) + ',' + str(node[1])
            if node_str not in visited:
                ret = ret + 1
                for d in dir:
                    row, col = node[0] + d[0], node[1] + d[1]
                    if 0 <= row < max_row and 0 <= col < max_col:
                        next_str = str(row) + ',' + str(col)
                        if lines[row][col] < 9 and next_str not in visited:
                            queue.append((row, col))
            visited[node_str] = True
            del queue[0]
        return ret
    count = 1
    l = []
    for low_point in low_points:
        a = bfs(low_point)
        l.append(a)
    l.sort()
    print(l[-1] * l[-2] * l[-3])