with open('day1_1.txt') as file:
    lines = file.readlines()
    prev = 0
    current = 0
    count = 0
    started = False
    for i in range(len(lines)):
        prev = current
        current = int(lines[i])
        if not started:
            started = True
            continue
        if current > prev:
            count += 1
    print(count)
