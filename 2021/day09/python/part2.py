def get_neighbours(x, y):
    neighbours = []
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if (x == 0 and dx == -1 or
                x == len(data[0]) - 1 and dx == 1 or
                y == 0 and dy == -1 or
                y == len(data) - 1 and dy == 1):
            continue
        neighbours.append((x + dx, y + dy))
    return neighbours


def dfs(x, y):
    if (x, y) in visited or data[y][x] == 9:
        return
    visited.add((x, y))
    for neighbour in get_neighbours(x, y):
        dfs(*neighbour)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [[int(x) for x in line] for line in f.read().splitlines()]

    count = 0
    visited = set()
    basin_sizes = []
    for i in range(len(data[0])):
        for ii in range(len(data)):
            if (i, ii) not in visited and data[ii][i] != 9:
                prev_len = len(visited)
                dfs(i, ii)
                basin_sizes.append(len(visited) - prev_len)

    basin_sizes.sort()
    print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])
