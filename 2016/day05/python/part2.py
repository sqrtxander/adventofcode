import hashlib


def solve(file):
    with open(file, 'r') as f:
        doorid = f.read()

    password = [None] * 8
    i = 0
    while None in password:
        hash_ = hashlib.md5(f'{doorid}{i}'.encode('utf-8')).hexdigest()
        pos = hash_[5]
        if hash_.startswith('00000') and pos.isdigit() and int(pos) < 8 and password[int(pos)] is None:
            password[int(pos)] = hash_[6]
            
        i += 1

    return ''.join(password)


if __name__ == '__main__':

    EXPECTED = '05ace8e3'
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
