def parse(file):
    with open(file, 'r') as f:
        data = [int(line) for line in f.read().splitlines()]
    return data


def solve(masses):
    return sum(mass // 3 - 2 for mass in masses)


if __name__ == '__main__':

    EXPECTED = 33583
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
