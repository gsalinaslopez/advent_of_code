def check_board_won(board):
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x' and board[0][3] == 'x' and board[0][4] == 'x':
        return True
    if board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x' and board[1][3] == 'x' and board[1][4] == 'x':
        return True
    if board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x' and board[2][3] == 'x' and board[2][4] == 'x':
        return True
    if board[3][0] == 'x' and board[3][1] == 'x' and board[3][2] == 'x' and board[3][3] == 'x' and board[3][4] == 'x':
        return True
    if board[4][0] == 'x' and board[4][1] == 'x' and board[4][2] == 'x' and board[4][3] == 'x' and board[4][4] == 'x':
        return True

    if board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x' and board[3][0] == 'x' and board[4][0] == 'x':
        return True
    if board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x' and board[3][1] == 'x' and board[4][1] == 'x':
        return True
    if board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x' and board[3][2] == 'x' and board[4][2] == 'x':
        return True
    if board[0][3] == 'x' and board[1][3] == 'x' and board[2][3] == 'x' and board[3][3] == 'x' and board[4][3] == 'x':
        return True
    if board[0][4] == 'x' and board[1][4] == 'x' and board[2][4] == 'x' and board[3][4] == 'x' and board[4][4] == 'x':
        return True

    return False


def check_score(board, winning_number):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'x':
                count += int(board[i][j])
    return int(count) * int(winning_number)


with open('day4_2.txt') as file:
    lines = file.readlines()
    bingo_stream = list(lines[0].strip().split(','))

    bingo_boards = []
    bingo_board_index = 0
    single_board = []
    num_map = {}

    for i in range(2, len(lines)):
        line = lines[i].strip()
        if (len(line) == 0):
            print('*****')
            bingo_boards.append(single_board)
            bingo_board_index += 1
            single_board = []
        else:
            row = [x for x in line.split(' ') if x != '']
            for n in row:
                if n not in num_map:
                    num_map[n] = [bingo_board_index]
                else:
                    num_map[n].append(bingo_board_index)

            single_board.append(row)

    bingo_boards.append(single_board)
    bingo_board_index += 1

    print("BOARDS")
    for i in range(bingo_board_index):
        print('******')
        for row in bingo_boards[i]:
            print(row)
        print('******')

    print(num_map, bingo_board_index)
    won = 0
    won_map = {}
    for n in bingo_stream:
        if n in num_map:
            for board_index in num_map[n]:
                # flag out that number from that board
                for i in range(len(bingo_boards[board_index])):
                    for j in range(len(bingo_boards[board_index][i])):
                        if bingo_boards[board_index][i][j] == n:
                            bingo_boards[board_index][i][j] = 'x'
                            if check_board_won(bingo_boards[board_index]):
                                if board_index not in won_map:
                                    won_map[board_index] = True
                                    won += 1
                                    print('winning board!', board_index, won)
                                    if won == bingo_board_index:
                                        print(check_score(bingo_boards[board_index], n))
                                        exit(0)