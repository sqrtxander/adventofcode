def solve(file):
    with open(file, 'r') as f:
        answers = [line.split('\n') for line in f.read().split('\n\n')]


    return sum(len(set(''.join(group))) for group in answers)


if __name__ == '__main__':

    EXPECTED = 11
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
