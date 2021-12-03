with open('day2_2.txt') as file:
    lines = file.readlines()
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        args = line.split(' ')
        command = args[0]
        val = int(args[1])
        if command == 'forward':
            horizontal += val
            depth += aim * val
        elif command == 'down':
            aim += val
        elif command == 'up':
            aim -= val
    print(horizontal * depth)