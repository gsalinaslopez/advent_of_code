with open('day3_1.txt') as file:
    lines = file.readlines()
    bits_freq = [[0, 0] for b in str(lines[0]).strip()]
    for line in lines:
        i = 0
        for b in str(line).strip():
            # print('b is', b)
            if b == '0':
                bits_freq[i][0] += 1
            elif b == '1':
                bits_freq[i][1] += 1
            i += 1
    gamma = []
    epsilon = []
    for b in bits_freq:
        if b[0] > b[1]:
            gamma.append('0')
            epsilon.append('1')
        else:
            epsilon.append('0')
            gamma.append('1')
    g = int(str(''.join(gamma)), 2)
    e = int(str(''.join(epsilon)), 2)
    print(g * e)