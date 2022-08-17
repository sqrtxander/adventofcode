def double_letter(num):
    number_str = str(num)
    last_digit = number_str[0]
    group_len = 1
    for digit in number_str[1:]:
        if digit == last_digit:
            group_len += 1
        else:
            if group_len == 2:
                return True
            last_digit = digit
            group_len = 1
    return group_len == 2


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
