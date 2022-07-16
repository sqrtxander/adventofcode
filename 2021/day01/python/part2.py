def solve(file):
    with open(file, 'r') as f:
        depths = [int(x) for x in f.readlines()]
    return sum(depths[i] > depths[i-3] for i in range(3, len(depths)))


if __name__ == '__main__':
    EXPECTED = 5
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
