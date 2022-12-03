import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 12
TEST_INPUT = '''\
A Y
B X
C Z
'''


def solve(inp):
    def score_outcome(elf, you):
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

    strategy_guide = [line.split() for line in inp.strip().splitlines()]

    return sum(score_outcome(elf, you) for elf, you in strategy_guide)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
