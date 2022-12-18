import os
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 26
TEST_INPUT = '''\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''
def distance(sx, sy, bx, by):
    return abs(bx - sx) + abs(by - sy)


def solve(inp, row=2000000):
    data = [[int(x1), int(y1), int(x2), int(y2)] for x1, y1, x2, y2 in re.findall(
        r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', inp.strip())]

    sensors = set()
    beacons = set()

    no_beacons = set()

    for sx, sy, bx, by in data:
        sensors.add((sx, sy))
        beacons.add((bx, by))

    for sx, sy, bx, by in data:
        d = distance(sx, sy, bx, by) 
        if not(d - sy <= row <= d + sy):
            continue
        width = d - abs(row - sy)
        for x_pos in range(sx - width, sx + width + 1):
            if (x_pos, row) not in beacons:
                no_beacons.add((x_pos, row))
    
    return len(no_beacons)

def main():
    test = solve(TEST_INPUT, 10)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
