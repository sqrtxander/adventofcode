def is_low(x, y):
    for nx, ny in get_neighbours(x, y):
        if data[y][x] >= data[ny][nx]:
            return False
    return int(data[y][x]) + 1


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


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [[int(x) for x in line] for line in f.read().splitlines()]

    count = 0
    for i in range(len(data)):
        for ii in range(len(data[0])):
            if is_low(ii, i):
                count += is_low(ii, i)

    print(count)
