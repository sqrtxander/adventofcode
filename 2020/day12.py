data = [line.strip() for line in open('inputs/input12.txt').readlines()]

dirs = ('N', 'E', 'S', 'W')
x, y = 0, 0
facing = 'E'
for instruction in data:
    direc = instruction[0]
    dist = int(instruction[1:])

    if direc == 'F':
        direc = facing

    if direc == 'L':
        facing = dirs[(dirs.index(facing) - dist//90) % 4]
    elif direc == 'R':
        facing = dirs[(dirs.index(facing) + dist//90) % 4]

    elif direc == 'N':
        y += dist
    elif direc == 'E':
        x += dist
    elif direc == 'S':
        y -= dist
    elif direc == 'W':
        x -= dist

print(f'Part 1: {abs(x) + abs(y)}')

sx, sy = 0, 0
wx, wy = 10, 1
for instruction in data:
    direc = instruction[0]
    dist = int(instruction[1:])

    if direc == 'F':
        sx, wx = sx + (wx - sx) * dist, wx + (wx - sx) * dist
        sy, wy = sy + (wy - sy) * dist, wy + (wy - sy) * dist

    elif direc == 'L':
        for _ in range(dist // 90):
            wx, wy = sx - (wy - sy), sy + (wx - sx)
    elif direc == 'R':
        for _ in range(dist // 90):
            wx, wy = sx + (wy - sy), sy - (wx - sx)

    elif direc == 'N':
        wy += dist
    elif direc == 'E':
        wx += dist
    elif direc == 'S':
        wy -= dist
    elif direc == 'W':
        wx -= dist

print(f'Part 2: {abs(sx) + abs(sy)}')
