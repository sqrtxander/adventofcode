import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 15
TEST_INPUT = '''\
A Y
B X
C Z
'''


def solve(inp):
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

    strategy_guide = [line.split() for line in inp.strip().splitlines()]

    return sum(score_outcome(elf, you) for elf, you in strategy_guide)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
