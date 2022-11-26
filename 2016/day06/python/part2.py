from collections import Counter


def solve(file):
    with open(file, 'r') as f:
        columns = zip(*f.read().splitlines())

    return ''.join([Counter(col).most_common()[-1][0] for col in columns])


if __name__ == '__main__':

    EXPECTED = 'advent'
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
