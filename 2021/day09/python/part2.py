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
    def dfs(x, y):
        if (x, y) in visited or heightmap[y][x] == 9:
            return
        visited.add((x, y))
        for neighbour in get_neighbours(x, y, heightmap):
            dfs(*neighbour)

    visited = set()
    basin_sizes = []
    for x in range(len(heightmap[0])):
        for y in range(len(heightmap)):
            if (x, y) not in visited and heightmap[y][x] != 9:
                prev_len = len(visited)
                dfs(x, y)
                basin_sizes.append(len(visited) - prev_len)

    basin_sizes.sort()
    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]


if __name__ == '__main__':

    EXPECTED = 1134
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
