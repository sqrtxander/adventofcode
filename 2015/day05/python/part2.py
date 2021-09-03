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


def is_nice(string):
    return duo_twice(string) and repeat_between(string)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        strings = tuple(x.strip() for x in f.readlines())

    nice = sum(is_nice(string) for string in strings)

    print(nice)