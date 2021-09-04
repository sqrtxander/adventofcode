import copy


def get_neighbours(table, x, y):
    count = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx != 0 or dy != 0:
                if 0 <= y + dy < len(table) and 0 <= x + dx < len(table[0]):
                    if table[y + dy][x + dx]:
                        count += 1
    return count


if __name__ == '__main__':
    lights = []
    with open('../input.txt', 'r') as f:
        for line in f:
            line = line.replace('#', '1').replace('.', '0').strip()
            lights.append([int(x) for x in line])

    for _ in range(100):
        prev_lights = copy.deepcopy(lights)
        for x in range(len(lights[0])):
            for y in range(len(lights)):
                n = get_neighbours(prev_lights, x, y)
                if prev_lights[y][x]:
                    if n not in (2, 3):
                        lights[y][x] = 0
                else:
                    if n == 3:
                        lights[y][x] = 1

    print(sum(sum(x) for x in lights))
