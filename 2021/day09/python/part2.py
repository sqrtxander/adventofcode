def get_neighbours(x, y):
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if x + dx < 0 or x + dx >= len(heightmap[0]):
            continue
        if y + dy < 0 or y + dy >= len(heightmap[0]):
            continue
        yield x + dx, y + dy


def dfs(x, y):
    if (x, y) in visited or heightmap[y][x] == 9:
        return
    visited.add((x, y))
    for neighbour in get_neighbours(x, y):
        dfs(*neighbour)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        heightmap = [[int(num) for num in line] for line in f.read().splitlines()]

    visited = set()
    basin_sizes = []
    for x in range(len(heightmap[0])):
        for y in range(len(heightmap)):
            if (x, y) not in visited and heightmap[x][y] != 9:
                prev_len = len(visited)
                dfs(x, y)
                basin_sizes.append(len(visited) - prev_len)

    basin_sizes.sort()
    print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])
