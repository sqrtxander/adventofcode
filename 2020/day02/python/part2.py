import re


def solve(file):
    with open(file, 'r') as f:
        data = [(int(a), int(b), c, d) for a, b, c, d in
                re.findall(r'(\d+)-(\d+) (\w): (\w+)', f.read())]

    return sum((password[rulel-1] == key) ^ (password[ruleu-1] == key)
               for rulel, ruleu, key, password in data)


if __name__ == '__main__':

    EXPECTED = 1
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
