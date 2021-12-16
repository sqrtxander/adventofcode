def get_neighbours(x, y, heightmap):
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if x + dx < 0 or x + dx >= len(heightmap[0]):
            continue
        if y + dy < 0 or y + dy >= len(heightmap):
            continue
        yield x + dx, y + dy


def is_low(x, y, heightmap):
    for nx, ny in get_neighbours(x, y, heightmap):
        if heightmap[y][x] >= heightmap[ny][nx]:
            return False
    return int(heightmap[y][x]) + 1


def parse(file):
    with open(file, 'r') as f:
        data = [[int(num) for num in line] for line in f.read().splitlines()]
    return data


def solve(heightmap):
    count = sum(sum(is_low(x, y, heightmap) for x in range(len(heightmap[0]))) for y in range(len(heightmap)))
    return count


if __name__ == '__main__':

    EXPECTED = 15
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))

