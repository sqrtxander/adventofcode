import numpy as np
import copy

test = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''
data = [list(x.strip()) for x in test.split('\n')]
# data = [list(x.strip()) for x in open('inputs/input11.txt').readlines()]
# print(np.matrix(data))
width = len(data[0])
height = len(data)
print(width, height)


def change_to(x, y):
    xl = x - 1 if x >= 1 else 0
    yl = y - 1 if y >= 1 else 0
    xu = x + 2 if x <= width - 2 else width
    yu = y + 2 if y <= height - 2 else height

    if data[y][x] == 'L':

        for i in range(xl, xu):
            for j in range(yl, yu):
                if data[j][i] == '#' and i != x and j != y:
                    return 'L'
        return '#'
    elif data[y][x] == '#':
        occ_count = 0
        for i in range(xl, xu):
            for j in range(yl, yu):
                if data[j][i] == '#' and i != x and j != y:
                    occ_count += 1
        return 'L' if occ_count >= 4 else '#'


while True:
    # next_data = data.copy()
    next_data = copy.deepcopy(data)
    for x in range(width):
        for y in range(height):
            if data[y][x] != '.':
                next_data[y][x] = change_to(x, y)
    print(np.matrix(next_data))

    if data == next_data:
        break
    # data = next_data[:]
    data = copy.deepcopy(next_data)
occ_count = 0
for x in range(width):
    for y in range(height):
        if next_data[y][x] == '#':
            occ_count += 1

print(occ_count)

# not 2131


def bounds(x, y):
    xl = x - 1 if x >= 1 else 0
    yl = y - 1 if y >= 1 else 0
    xu = x + 2 if x <= width - 1 else width
    yu = y + 2 if y <= height - 1 else height
    return xl, yl, xu, yu

# print(bounds(3, ))

for x in range(0, 2):
    print(x)