import re

password = 'hepxcrrq'

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def increment_pass(pw, index=1):
    try:
        pos = alphabet.index(password[-index])
        pw = (list(pw))
        pw[-index] = alphabet[pos + 1]
        pw = ''.join(pw)
        return pw
    except IndexError:
        pw = (list(pw))
        pw[-index] = alphabet[0]
        pw = ''.join(pw)
        return increment_pass(pw, index+1)


def valid(pw):
    # contains a straight of 3
    if not any(pw[straight:straight+3] in alphabet for straight in range(len(pw) - 2)):
        return False

    # no i, o, l
    if any(char in pw for char in ('i', 'o', 'l')):
        return False

    # contains 2 different double letters
    if not len(re.findall(r'(.)\1', pw)) >= 2:
        return False

    return True


while not valid(password):
    password = increment_pass(password)

print(f'Part 1: {password}')

password = increment_pass(password)
while not valid(password):
    password = increment_pass(password)

print(f'Part 2: {password}')
