import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 21
TEST_INPUT = '''\
30373
25512
65332
33549
35390
'''


def solve(inp):
    def up(x, y):
        for i in range(y, 0, -1):
            if treemap[(x, y)] <= treemap[(x, i-1)]:
                return False
        return True

    def right(x, y):
        for i in range(x, width-1):
            if treemap[(x, y)] <= treemap[(i+1, y)]:
                return False
        return True

    def down(x, y):
        for i in range(y, height-1):
            if treemap[(x, y)] <= treemap[(x, i+1)]:
                return False
        return True

    def left(x, y):
        for i in range(x, 0, -1):
            if treemap[(x, y)] <= treemap[(i-1, y)]:
                return False
        return True

    def is_visible(x, y):
        return up(x, y) or right(x, y) or down(x, y) or left(x, y)

    data = inp.strip().splitlines()
    width, height = len(data[0]), len(data)
    treemap = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            treemap[(x, y)] = int(char)

    total = width * 2 + height * 2 - 4
    for y in range(1, height-1):
        for x in range(1, width-1):
            total += is_visible(x, y)
    return total


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
