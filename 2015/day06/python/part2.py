import numpy as np
import re


def turnon(x1, y1, x2, y2, matrix):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            matrix[y][x] += 1
    return matrix


def turnoff(x1, y1, x2, y2, matrix):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            matrix[y][x] -= 1
            if matrix[y][x] <0:
                matrix[y][x] = 0
    return matrix


def toggle(x1, y1, x2, y2, matrix):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            matrix[y][x] += 2
    return matrix


if __name__ == '__main__':

    with open('../input.txt', 'r') as f:
        instructions = [(a, (int(b), int(c),), (int(d), int(e))) for a, b, c, d, e in re.findall(r'([\w ]+) (\d+),(\d+) through (\d+),(\d+)', f.read())]

    lights = np.zeros((1000, 1000), dtype=np.int)

    for instruction, (x1, y1), (x2, y2) in instructions:
        if instruction == 'turn on':
            lights = turnon(x1, y1, x2, y2, lights)

        elif instruction == 'turn off':
            lights = turnoff(x1, y1, x2, y2, lights)

        elif instruction == 'toggle':
            lights = toggle(x1, y1, x2, y2, lights)

    print(np.sum(lights))

