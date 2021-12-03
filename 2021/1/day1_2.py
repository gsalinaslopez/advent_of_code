with open('day1.txt') as file:
    lines = file.readlines()
    prev = 0
    current = 0
    count = 0
    started = False
    for i in range(2, len(lines)):
        prev = current
        current = int(lines[i]) + int(lines[i - 1]) + int(lines[i - 2])
        if not started:
            started = True
            continue
        if current > prev:
            count += 1
    print(count)
