def parse(file):
    with open(file, 'r') as f:
        data = [int(line) for line in f.read().splitlines()]
    return data


def solve(masses):
    total = 0
    for mass in masses:
        while True:
            mass = mass // 3 - 2
            if mass <= 0:
                break
            total += mass
    return total


if __name__ == '__main__':

    EXPECTED = 50346
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
