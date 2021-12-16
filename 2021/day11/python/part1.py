def get_neighbours(x, y, octopi):
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
            for nx, ny in get_neighbours(x, y, octopi):
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


def parse(file):
    with open(file, 'r') as f:
        data = [[int(num) for num in line] for line in f.read().splitlines()]
    return data


def solve(octopi):
    flash_num = 0

    for _ in range(100):
        octopi = [[num + 1 for num in line] for line in octopi]
        octopi = flash(octopi)
        flash_num += sum(line.count(0) for line in octopi)

    return flash_num


if __name__ == '__main__':

    EXPECTED = 1656
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
