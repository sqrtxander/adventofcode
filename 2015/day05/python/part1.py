def vowel_count(string):
    return sum(string.count(v) for v in 'aeiou')


def double_letter(string):
    for pos in range(1, len(string)):
        if string[pos] == string[pos - 1]:
            return True
    return False


def no_disallowed(string):
    return not any(s in string for s in ('ab', 'cd', 'pq', 'xy'))


def is_nice(string):
    return vowel_count(string) >= 3 and double_letter(string) and no_disallowed(string)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        strings = tuple(x.strip() for x in f.readlines())

    nice = sum(is_nice(string) for string in strings)

    print(nice)