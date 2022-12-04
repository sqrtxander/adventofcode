import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 2
TEST_INPUT = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''


def solve(inp):
    def fully_contained(a, b, c, d):
        return a <= c and b >= d or a >= c and b <= d

    data = [[[int(num) for num in part.split('-')]
             for part in line.split(',')] for line in inp.strip().splitlines()]

    return sum(fully_contained(a, b, c, d) for (a, b,), (c, d) in data)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
