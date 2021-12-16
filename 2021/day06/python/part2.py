from collections import Counter


def parse(file):
    with open(file, 'r') as f:
        data = Counter([int(num) for num in f.read().split(',')])
    return data


def solve(ages):

    for _ in range(256):
        ages = {n: ages[n + 1] for n in range(-1, 8)}
        ages[8] = ages[-1]
        ages[6] += ages[-1]
        ages[-1] = 0

    return sum(ages.values())



if __name__ == '__main__':

    EXPECTED = 26984457539
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
