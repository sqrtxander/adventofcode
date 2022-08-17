def double_letter(num):
    prev_pos = ''
    for i in str(num):
        if i == prev_pos:
            return True
        prev_pos = i
    return False


def no_decrease(num):
    prev_pos = 0
    for i in str(num):
        if int(i) < prev_pos:
            return False
        prev_pos = int(i)
    return True


def solve(file):
    with open(file, 'r') as f:
        lower, upper = [int(num) for num in f.read().split('-')]

    return sum([double_letter(num) and no_decrease(num) for num in range(lower, upper + 1)])


if __name__ == '__main__':

    print(solve('../input.in'))
