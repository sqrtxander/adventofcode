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
            if treemap[(x, y)] <= treemap[(x, i-1)]:
                return trees + 1
            elif treemap[(x, y)] > treemap[(x, i-1)]:
                trees += 1
        return trees

    def right(x, y):
        trees = 0
        for i in range(x, width-1):
            if treemap[(x, y)] <= treemap[(i+1, y)]:
                return trees + 1
            elif treemap[(x, y)] > treemap[(i+1, y)]:
                trees += 1
        return trees

    def down(x, y):
        trees = 0
        for i in range(y, height-1):
            if treemap[(x, y)] <= treemap[(x, i+1)]:
                return trees + 1
            elif treemap[(x, y)] > treemap[(x, i+1)]:
                trees += 1
        return trees

    def left(x, y):
        trees = 0
        for i in range(x, 0, -1):
            if treemap[(x, y)] <= treemap[(i-1, y)]:
                return trees + 1
            elif treemap[(x, y)] > treemap[(i-1, y)]:
                trees += 1
        return trees

    def get_scenic_score(x, y):
        return up(x, y) * right(x, y) * down(x, y) * left(x, y)

    data = inp.strip().splitlines()
    width, height = len(data[0]), len(data)
    treemap = {}
    for x in range(width):
        for y in range(height):
            treemap[(x, y)] = int(data[y][x])

    return max(get_scenic_score(x, y) for x in range(1, width-1) for y in range(1, height-1))


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
