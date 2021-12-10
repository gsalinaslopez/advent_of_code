unique_lens = {2: 1, 3: 7, 4: 4, 7: 8}

with open('day8_1.txt') as file:
    lines = file.readlines()
    count = 0
    for line in lines:
        entry = line.strip().split('|')
        for guess in entry[1].split(' '):
            if len(guess) in unique_lens:
                count += 1
    print(count)