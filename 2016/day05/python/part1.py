import hashlib


def solve(file):
    with open(file, 'r') as f:
        doorid = f.read()

    password = ''
    i = 0
    while len(password) < 8:
        hash_ = hashlib.md5(f'{doorid}{i}'.encode('utf-8')).hexdigest()
        if hash_.startswith('00000'):
            password += hash_[5]
        i += 1

    return password


if __name__ == '__main__':

    EXPECTED = '18f47a30'
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
