import os
from collections import defaultdict


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 24
TEST_INPUT = '''\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''


def sandfall(x, y, scan):
    if not scan[(x, y+1)]:
        return x, y+1

    elif not scan[(x-1, y+1)]:
        return x-1, y+1

    elif not scan[(x+1, y+1)]:
        return x+1, y+1

    return None


def solve(inp):
    maxy = 0
    scan = defaultdict(bool)
    for line in inp.strip().splitlines():
        coords = line.split(' -> ')
        for i in range(len(coords)-1):
            x1, y1 = (int(c) for c in coords[i].split(','))
            x2, y2 = (int(c) for c in coords[i+1].split(','))
            maxy = max(maxy, y1, y2)
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    scan[(x1, i)] = True
            else:
                for i in range(min(x1, x2), (max(x1, x2) + 1)):
                    scan[(i, y1)] = True

    sand_count = 0
    y = 0
    while y < maxy:
        x, y = 500, 0
        fall = sandfall(x, y, scan)
        while fall is not None and y < maxy:
            x, y = fall
            fall = sandfall(x, y, scan)
        sand_count += 1
        scan[(x, y)] = True

    return sand_count - 1


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
