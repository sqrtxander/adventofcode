def get_neighbours(x, y):
    for dx, dy in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        if x + dx < 0 or x + dx >= len(octopi[0]):
            continue
        if y + dy < 0 or y + dy >= len(octopi):
            continue
        yield x + dx, y + dy


def flash(octopi):
    flashed = set()
    while True:
        greater = all_greater_9(octopi, flashed)
        if not greater:
            break

        for x, y in greater:
            for nx, ny in get_neighbours(x, y):
                octopi[ny][nx] += 1
            flashed.add((x, y))

    for x, y in flashed:
        octopi[y][x] = 0
    return octopi


def all_greater_9(octopi, flashed):
    greater = set()
    for y in range(len(octopi)):
        for x in range(len(octopi[0])):
            if octopi[y][x] > 9 and (x, y) not in flashed:
                greater.add((x, y))
    return greater


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        octopi = [[int(num) for num in line] for line in f.read().splitlines()]

    flash_num = 0

    for _ in range(100):
        octopi = [[num + 1 for num in line] for line in octopi]
        octopi = flash(octopi)
        flash_num += sum(sum(num == 0 for num in line) for line in octopi)

    print(flash_num)