def solve(file):
    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]
    return data


if __name__ == '__main__':

    EXPECTED = 0
    test = solve('test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('input.in'))
