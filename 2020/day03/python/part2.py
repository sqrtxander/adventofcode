def count_trees(treemap, right, down):
    width = len(treemap[0])
    x = right % width
    y = down
    count = 0
    while y < len(treemap):
        if treemap[y][x] == '#':
            count += 1
        x = (x + right) % width
        y += down
    return count


def solve(file):
    with open(file, 'r') as f:
        treemap = f.read().splitlines()

    count = 1
    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        count *= count_trees(treemap, right, down)

    return count

if __name__ == '__main__':

    EXPECTED = 336
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
