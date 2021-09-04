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

    lights[0][0] = lights[len(lights)-1][0] = lights[0][len(lights[0])-1] = lights[len(lights)-1][len(lights[0])-1] = 1

    for _ in range(100):
        prev_lights = copy.deepcopy(lights)
        for x in range(len(lights[0])):
            for y in range(len(lights)):
                if (x, y) not in ((0, 0), (0, len(lights)-1), (len(lights[0])-1, 0), (len(lights[0])-1, len(lights)-1)):
                    n = get_neighbours(prev_lights, x, y)
                    if prev_lights[y][x]:
                        if n not in (2, 3):
                            lights[y][x] = 0
                    else:
                        if n == 3:
                            lights[y][x] = 1

    print(sum(sum(x) for x in lights))
