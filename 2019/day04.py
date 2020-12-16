data_lower = 134564
data_upper = 585159


def double_letter_1(num):
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


def double_letter_2(num):
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


def check_passwords_1():
    count = 0
    for num in range(data_lower, data_upper):
        if len(str(num)) == 6 and double_letter_1(num) and no_decrease(num):
            count += 1
    return count


def check_passwords_2():
    count = 0
    for num in range(data_lower, data_upper):
        if len(str(num)) == 6 and double_letter_2(num) and no_decrease(num):
            count += 1
    return count


print(f'Part 1: {check_passwords_1()}')
print(f'Part 2: {check_passwords_2()}')
