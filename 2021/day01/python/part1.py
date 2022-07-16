def solve(file):
    with open(file, 'r') as f:
        depths = [int(x) for x in f.readlines()]
    return sum(depths[i] > depths[i-1] for i in range(1, len(depths)))


if __name__ == '__main__':
    EXPECTED = 7
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
