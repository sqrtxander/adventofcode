from collections import defaultdict


def parse(file):
    with open(file, 'r') as f:
        data = [[tuple(map(int, num.split(','))) for num in line.split(' -> ')]
                for line in f.read().splitlines()]
    return data


def solve(data):
    lines = defaultdict(int)

    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1

            for y in range(y1, y2 + 1):
                lines[(x1, y)] += 1

        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1

            for x in range(x1, x2 + 1):
                lines[(x, y1)] += 1

        else:
            flipped = False

            if x1 > x2:
                x1, x2 = x2, x1
                flipped = not flipped
            if y1 > y2:
                y1, y2 = y2, y1
                flipped = not flipped

            if flipped:
                pipe_coords = zip(reversed(range(x1, x2 + 1)), range(y1, y2 + 1))
            else:
                pipe_coords = zip(range(x1, x2 + 1), range(y1, y2 + 1))

            for x, y in pipe_coords:
                lines[(x, y)] += 1

    return sum(x > 1 for x in lines.values())


if __name__ == '__main__':

    EXPECTED = 12
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))

