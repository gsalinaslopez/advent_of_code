unique_lens = {2: 1, 3: 7, 4: 4, 7: 8}

with open('day8_1.txt') as file:
    lines = file.readlines()
    count = 0
    for line in lines:
        entry = line.strip().split('|')
        guessed = {}
        not_guessed = {}
        segments = {}
        for guess in entry[0].strip().split(' '):
            if len(guess) in unique_lens.keys():
                guessed[unique_lens[len(guess)]] = guess
            else:
                if len(guess) not in not_guessed:
                    not_guessed[len(guess)] = []
                not_guessed[len(guess)].append(guess)
        # guess for the '1' segment
        for c in guessed[7]:
            if c not in guessed[1]:
                segments[1] = c
                break
        # guess for the '7' segment
        # by looking into the potential number 3 (len 5)
        four_and_top = set(guessed[4]).union(set(segments[1]))
        for three in not_guessed[5]:
            segment_seven = set(three) - four_and_top
            if len(segment_seven) == 1:
                for seven in segment_seven:
                    segments[7] = seven
        # guess for the '5' segment
        # by looking into number 8
        four_and_top_bottom = set(guessed[4]).union(set(segments[1])).union(set(segments[7]))
        segment_five = set(guessed[8]) - four_and_top_bottom
        for five in segment_five:
            segments[5] = five
        # guess for the '6' segment
        # by looking into number 5
        eight_minus_one_and_bottom_left = set(guessed[8]) - set(guessed[1]) - set(segments[5])
        for five in not_guessed[5]:
            segment_six = set(five) - eight_minus_one_and_bottom_left
            if len(segment_six) == 1:
                for six in segment_six:
                    segments[6] = six
        # guess for the number 6
        eight_minus_one_plus_segment_six = (set(guessed[8]) - set(guessed[1])).union(set(segments[6]))
        for i in range(len(not_guessed[6])):
            six = not_guessed[6][i]
            if set(six) == eight_minus_one_plus_segment_six:
                guessed[6] = ''.join(set(six))
                del not_guessed[6][i]
                break
        # guess for the '3' segment
        # by looking into number 0 or 9
        for zero in not_guessed[6]:
            segment_three = set(zero) - set(guessed[6])
            for three in segment_three:
                segments[3] = three
        # guess for the '4' segment
        if (set(not_guessed[6][0]) - set(not_guessed[6][1])) != set(segments[5]):
            segments_four = set(not_guessed[6][0]) - set(not_guessed[6][1])
            for four in segments_four:
                segments[4] = four
        if (set(not_guessed[6][1]) - set(not_guessed[6][0])) != set(segments[5]):
            segments_four = set(not_guessed[6][1]) - set(not_guessed[6][0])
            for four in segments_four:
                segments[4] = four
        # guess for the '2' segment
        segment_two = set(guessed[8]) - set(segments.values())
        for two in segment_two:
            segments[2] = two

        # segment set to number
        zero = {segments[1], segments[2], segments[3], segments[5], segments[6], segments[7]}
        one = {segments[3], segments[6]}
        two = {segments[1], segments[3], segments[4], segments[5], segments[7]}
        three = {segments[1], segments[3], segments[4], segments[6], segments[7]}
        four = {segments[2], segments[3], segments[4], segments[6]}
        five = {segments[1], segments[2], segments[4], segments[6], segments[7]}
        six = {segments[1], segments[2], segments[4], segments[5], segments[6], segments[7]}
        seven = {segments[1], segments[3], segments[6]}
        eight = {segments[1], segments[2], segments[3], segments[4], segments[5], segments[6], segments[7]}
        nine = {segments[1], segments[2], segments[3], segments[4], segments[6], segments[7]}
        displayed = []
        for display in entry[1].strip().split(' '):
            if set(display) == zero:
                displayed.append(0)
            if set(display) == one:
                displayed.append(1)
            if set(display) == two:
                displayed.append(2)
            if set(display) == three:
                displayed.append(3)
            if set(display) == four:
                displayed.append(4)
            if set(display) == five:
                displayed.append(5)
            if set(display) == six:
                displayed.append(6)
            if set(display) == seven:
                displayed.append(7)
            if set(display) == eight:
                displayed.append(8)
            if set(display) == nine:
                displayed.append(9)
        displayed = [str(x) for x in displayed]
        displayed = int(''.join(displayed))
        count += displayed
    print(count)
