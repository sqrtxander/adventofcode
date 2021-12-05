def check_off_num(num, boards):
    for i, board in enumerate(boards):
        for ii, row in enumerate(board):
            for iii, n in enumerate(row):
                if n == num:
                    boards[i][ii][iii] = 'X'
    return boards


def is_bingo(board):
    # horizontal
    for r in board:
        if r.count('X') == len(r):
            return board

    # vertical
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == 'X':
            return board

    return False


def score_board(board):
    return sum(sum(int(num) for num in row if num != 'X') for row in board)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        nums, *boards = f.read().split('\n\n')
        nums = nums.split(',')
        boards = [[row.split() for row in board.split('\n')]for board in boards]

    curr_num = board = None

    for curr_num in nums:
        check_off_num(curr_num, boards)

        for board in boards:
            if is_bingo(board):
                break
        else:
            continue
        break

    board_sum = score_board(board)

    print(board_sum * int(curr_num))
