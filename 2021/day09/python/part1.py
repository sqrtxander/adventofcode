def get_neighbours(x, y):
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if x + dx < 0 or x + dx >= len(heightmap[0]):
            continue
        if y + dy < 0 or y + dy >= len(heightmap[0]):
            continue
        yield x + dx, y + dy


def is_low(x, y):
    for nx, ny in get_neighbours(x, y):
        if heightmap[y][x] >= heightmap[ny][nx]:
            return False
    return int(heightmap[y][x]) + 1


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        heightmap = [[int(num) for num in line] for line in f.read().splitlines()]

    count = sum(sum(is_low(x, y) for x in range(len(heightmap[0]))) for y in range(len(heightmap)))
    print(count)
