def solve(file):
    def score_outcome(you, elf):
        scores = {'X': 0, 'Y': 3, 'Z': 6}

        # scissors
        if (elf, you) in (('A', 'X'), ('B', 'Z'), ('C', 'Y')):
            return scores[you] + 3
        # paper
        elif (elf, you) in (('A', 'Z'), ('B', 'Y'), ('C', 'X')):
            return scores[you] + 2
        # rock
        else:
            return scores[you] + 1

    with open(file, 'r') as f:
        data = [line.split() for line in f.read().splitlines()]

    return sum(score_outcome(you, elf) for elf, you in data)


if __name__ == '__main__':

    EXPECTED = 12
    test = solve('test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('input.in'))
