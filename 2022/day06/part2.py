import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 19
TEST_INPUT = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''


def solve(inp):
    for i in range(14, len(inp)):
        section = inp[i-14:i]
        if len(set(section)) == 14:
            return i


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
