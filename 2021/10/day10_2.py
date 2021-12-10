open_close_map = {')': '(', ']': '[', '}': '{', '>': '<'}
close_open_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
close_price = { ')': 1, ']': 2, '}': 3, '>': 4}

with open('day10_2.txt') as file:
    lines = file.readlines()
    l = []
    for line in lines:
        entry = line.strip()
        stack = []
        broke = False
        for c in entry:
            if c in open_close_map.values():
                stack.append(c)
            elif open_close_map[c] == stack[-1]:
                del stack[-1]
            else:
                broke = True
                break
        if not broke:
            count = 0
            for i in reversed(range(len(stack))):
                count = (count * 5) + close_price[close_open_map[stack[i]]]
            l.append(count)
    l.sort()
    print(l[(len(l) - 1)// 2])