def solve(file):
    with open(file, 'r') as f:
        nums = set(int(line) for line in f.read().splitlines())

    for i in nums:
        if 2020 - i in nums:
            return i * (2020 - i)


if __name__ == '__main__':

    EXPECTED = 514579
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
