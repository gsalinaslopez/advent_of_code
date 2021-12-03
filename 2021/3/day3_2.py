import copy


def get_rating(lines, arg):
    bit_index = 0
    while(len(lines) > 1):
        bits_freq = [0, 0]
        zero = []
        one = []
        for line in lines:
            l = str(line).strip()
            b = l[bit_index : bit_index + 1]
            if b == '0':
                bits_freq[0] += 1
                zero.append(str(line))
            elif b == '1':
                bits_freq[1] += 1
                one.append(str(line))
        if arg == 'oxygen':
            if bits_freq[0] > bits_freq[1]:
                lines = zero
            else:
                lines = one
        if arg == 'co2':
            if bits_freq[0] <= bits_freq[1]:
                lines = zero
            else:
                lines = one

        bit_index += 1
    return str(lines[0]).strip()


with open('day3_2.txt') as file:
    lines = file.readlines()
    oxygen = int(str(get_rating(lines, 'oxygen')), 2)
    co2 = int(str(get_rating(lines, 'co2')), 2)
    print(oxygen * co2)
