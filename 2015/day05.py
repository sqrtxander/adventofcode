data = open('inputs/input05.txt').read().strip().split('\n')


def vowel_count(string):
    return list(string).count('a') + list(string).count('e') + list(string).count('i') \
           + list(string).count('o') + list(string).count('u')


def double_letter(string):
    for pos in range(1, len(string)):
        if string[pos] == string[pos - 1]:
            return True
    return False


def no_disallowed(string):
    return not any(s in string for s in ('ab', 'cd', 'pq', 'xy'))


def is_nice_string_1(string):
    return vowel_count(string) >= 3 and double_letter(string) and no_disallowed(string)


def duo_twice(string):
    for x in range(len(string)):
        duo = string[x:x+2]
        for y in range(x + 2, len(string)):
            if duo == string[y:y+2]:
                return True
    return False


def repeat_between(string):
    for pos in range(2, len(string)):
        if string[pos] == string[pos - 2]:
            return True
    return False


def is_nice_string_2(string):
    return duo_twice(string) and repeat_between(string)


nice_count_1 = 0
for i in data:
    if is_nice_string_1(i):
        nice_count_1 += 1

nice_count_2 = 0
for i in data:
    if is_nice_string_2(i):
        nice_count_2 += 1

print(f'Part 1: {nice_count_1}')
print(f'Part 2: {nice_count_2}')
