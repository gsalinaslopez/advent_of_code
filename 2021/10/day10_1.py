open_close_map = {')': '(', ']': '[', '}': '{', '>': '<'}
close_price = { ')': 3, ']': 57, '}': 1197, '>': 25137}

with open('day10_1.txt') as file:
    lines = file.readlines()
    stack = []
    count = 0
    for line in lines:
        entry = line.strip()
        for c in entry:
            if c in open_close_map.values():
                stack.append(c)
            elif open_close_map[c] == stack[-1]:
                del stack[-1]
            else:
                count += close_price[c]
                break
    print(count)