from copy import deepcopy

data = [list(x.strip()) for x in open('inputs/input11.txt').readlines()]
width = len(data[0])
height = len(data)


def change_to_1(x, y):
    occ_count = 0
    for xx in (-1, 0, 1):
        for yy in (-1, 0, 1):
            if not(xx == 0 and yy == 0):
                xp = x + xx
                yp = y + yy
                if 0 <= xp < width and 0 <= yp < height and data[yp][xp] == '#':
                    occ_count += 1
    if data[y][x] == 'L':
        return '#' if occ_count == 0 else 'L'
    elif data[y][x] == '#':
        return 'L' if occ_count >= 4 else '#'


def change_to_2(x, y):
    occ_count = 0
    for xd, yd in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
        xx = x
        yy = y
        xx += xd
        yy += yd
        if 0 <= xx < width and 0 <= yy < height and data[yy][xx] == '.':
            xx += xd
            yy += yd
            if not(0 <= xx < width and 0 <= yy < height):
                continue
            while data[yy][xx] == '.':
                xx += xd
                yy += yd
                if not(0 <= xx < width and 0 <= yy < height):
                    break
            if not(0 <= xx < width and 0 <= yy < height):
                continue
        if not(0 <= xx < width and 0 <= yy < height):
            continue
        if data[yy][xx] == '#':
            occ_count += 1

    if data[y][x] == 'L':
        return '#' if occ_count == 0 else 'L'
    elif data[y][x] == '#':
        return 'L' if occ_count >= 5 else '#'


while True:
    next_data = deepcopy(data)
    for x in range(width):
        for y in range(height):
            if data[y][x] != '.':
                next_data[y][x] = change_to_1(x, y)

    if data == next_data:
        break
    data = deepcopy(next_data)

occ_count = 0
for x in data:
    for y in x:
        if y == '#':
            occ_count += 1

print(f'Part 1: {occ_count}')

data = [list(x.strip()) for x in open('inputs/input11.txt').readlines()]

while True:
    next_data = deepcopy(data)

    for x in range(width):
        for y in range(height):
            if data[y][x] != '.':
                next_data[y][x] = change_to_2(x, y)

    if data == next_data:
        break
    data = deepcopy(next_data)

occ_count = 0
for x in data:
    for y in x:
        if y == '#':
            occ_count += 1

print(f'Part 2: {occ_count}')