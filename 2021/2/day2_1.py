with open('day2.txt') as file:
    lines = file.readlines()
    horizontal = 0
    depth = 0
    for line in lines:
        args = line.split(' ')
        command = args[0]
        val = int(args[1])
        if command == 'forward':
            horizontal += val
        elif command == 'down':
            depth += val
        elif command == 'up':
            depth -= val
    print(horizontal * depth)