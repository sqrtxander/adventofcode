import re


def check_off_num(num, boards):
    for i, b in enumerate(boards):
        for ii, r in enumerate(b):
            for iii, n in enumerate(r):
                if n == num:
                    boards[i][ii][iii] = 'X'
    return boards


def check_bingo(b):
    # horizontal
    for r in b:
        if r.count('X') == len(r):
            return b

    # vertical
    for i in range(len(b)):
        if b[0][i] == b[1][i] == b[2][i] == b[3][i] == b[4][i] == 'X':
            return b

    return False


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = f.read().split('\n\n')
        nums = data[0].split(',')
        boards = [x.split('\n') for x in data[1:]]
        for i, b in enumerate(boards):
            for ii, r in enumerate(b):
                boards[i][ii] = list(re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', r)[0])

    curr_num = b = None

    for curr_num in nums:
        check_off_num(curr_num, boards)

        for b in boards:
            if check_bingo(b):
                if len(boards) > 1:
                    boards.remove(b)
                else:
                    break
        else:
            continue
        break

    board_sum = sum(sum(int(i) for i in ii if i != 'X') for ii in b)
    print(board_sum * int(curr_num))
