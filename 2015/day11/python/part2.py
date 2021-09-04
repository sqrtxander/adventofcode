import re


def increment_pass(pw, index=-1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    try:
        pos = alphabet.index(password[index])
        pw = (list(pw))
        pw[index] = alphabet[pos + 1]
        pw = ''.join(pw)
        return pw
    except IndexError:
        pw = (list(pw))
        pw[index] = alphabet[0]
        pw = ''.join(pw)
        return increment_pass(pw, index-1)


def straight_of_n(n, pw):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return any(pw[straight:straight+n] in alphabet for straight in range(len(pw) - n + 1))


def no_invalid(invalid, pw):
    return not any(char in pw for char in invalid)


def n_pairs(n, pw):
    return len(re.findall(r'(.)\1', pw)) >= n


def valid(pw):
    return straight_of_n(3, pw) and no_invalid('iol', pw) and n_pairs(2, pw)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        password = f.read().strip()

    while not valid(password):
        password = increment_pass(password)

    password = increment_pass(password)

    while not valid(password):
        password = increment_pass(password)

    print(password)

