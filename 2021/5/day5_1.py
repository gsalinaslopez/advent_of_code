with open('day5_1.txt') as file:
    lines = file.readlines()
    coord_map = {}
    count = 0
    max_row = float('-inf')
    max_col = float('-inf')
    for i in range(len(lines)):
        line = [x.strip() for x in lines[i].strip().split("->")]
        coord1 = line[0].split(',')
        coord2 = line[1].split(',')
        coord1[0] = int(coord1[0])
        coord1[1] = int(coord1[1])
        coord2[0] = int(coord2[0])
        coord2[1] = int(coord2[1])
        print(coord1[0], coord1[1], coord2[0], coord2[1])
        if max(coord1[0], coord2[0]) > max_col:
            max_col = max(coord1[0], coord2[0])
        if max(coord1[1], coord2[1]) > max_row:
            max_row = max(coord1[1], coord2[1])
        if coord1[0] == coord2[0] and coord1[1] == coord2[1]:
            continue
            """
            in_coord = ','.join(coord1)
            if in_coord not in coord_map:
                coord_map[in_coord] = 0
            else:
                count += 1
            coord_map[in_coord] = coord_map[in_coord] + 1
            """
        elif coord1[0] == coord2[0]:
            for row in range(min(coord1[1], coord2[1]), max(coord1[1], coord2[1]) + 1):
                in_coord = str(coord1[0]) + ',' + str(row)
                if in_coord not in coord_map:
                    coord_map[in_coord] = 0
                coord_map[in_coord] = coord_map[in_coord] + 1
        elif coord1[1] == coord2[1]:
            for col in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0]) + 1):
                in_coord = str(col) + ',' + str(coord1[1])
                #print(in_coord)
                if in_coord not in coord_map:
                    coord_map[in_coord] = 0
                coord_map[in_coord] = coord_map[in_coord] + 1
    count2 = 0
    for i in range(max_row + 1):
        for j in range(max_col + 1):
            in_coord = str(j) + ',' + str(i)
            if in_coord not in coord_map:
                print('. ', end='')
            else:
                if coord_map[in_coord] >= 2:
                    count2 += 1
                print(str(coord_map[in_coord]) + ' ', end='')
        print('\n')
    print(count)
    print(count2)
