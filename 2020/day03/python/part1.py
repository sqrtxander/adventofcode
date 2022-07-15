def solve(file):
    with open(file, 'r') as f:
        treemap = f.read().splitlines()

    right = 3
    down = 1

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

if __name__ == '__main__':

    EXPECTED = 7
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
