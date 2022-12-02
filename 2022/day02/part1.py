def solve(file):
    def score_outcome(elf, you):
        scores = {'X': 1, 'Y': 2, 'Z': 3}

        # win
        if (elf, you) in (('A', 'Y'), ('B', 'Z'), ('C', 'X')):
            return scores[you] + 6
        # draw
        elif (elf, you) in (('A', 'X'), ('B', 'Y'), ('C', 'Z')):
            return scores[you] + 3
        # lose
        else:
            return scores[you]

    with open(file, 'r') as f:
        data = [line.split() for line in f.read().splitlines()]

    return sum(score_outcome(elf, you) for elf, you in data)


if __name__ == '__main__':

    EXPECTED = 15
    test = solve('test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('input.in'))
