import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 8
TEST_INPUT = '''\
30373
25512
65332
33549
35390
'''


def solve(inp):
    def up(x, y):
        trees = 0
        for i in range(y, 0, -1):
            trees += 1
            if treemap[(x, y)] <= treemap[(x, i-1)]:
                break
        return trees

    def right(x, y):
        trees = 0
        for i in range(x, width-1):
            trees += 1
            if treemap[(x, y)] <= treemap[(i+1, y)]:
                break
        return trees

    def down(x, y):
        trees = 0
        for i in range(y, height-1):
            trees += 1
            if treemap[(x, y)] <= treemap[(x, i+1)]:
                break
        return trees

    def left(x, y):
        trees = 0
        for i in range(x, 0, -1):
            trees += 1
            if treemap[(x, y)] <= treemap[(i-1, y)]:
                break
        return trees

    def get_scenic_score(x, y):
        return up(x, y) * right(x, y) * down(x, y) * left(x, y)

    data = inp.strip().splitlines()
    width, height = len(data[0]), len(data)
    treemap = {}

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            treemap[(x, y)] = int(char)

    return max(get_scenic_score(x, y) for x in range(1, width-1) for y in range(1, height-1))


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
