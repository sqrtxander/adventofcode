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


def parse(file):
    with open(file, 'r') as f:
        nums, *boards = f.read().split('\n\n')
        nums = nums.split(',')
        boards = [[row.split() for row in board.split('\n')]for board in boards]
    return nums, boards


def solve(nums, boards):
    for curr_num in nums:
        check_off_num(curr_num, boards)

        for board in boards:
            if is_bingo(board):
                if len(boards) > 1:
                    boards.remove(board)
                else:
                    board_sum = score_board(board)
                    return board_sum * int(curr_num)


if __name__ == '__main__':

    EXPECTED = 1924
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))
