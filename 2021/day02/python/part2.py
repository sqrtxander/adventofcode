def parse(file):
    with open(file, 'r') as f:
        data = [(dir_, int(dist)) for dir_, dist in
                [line.split() for line in f.read().splitlines()]]
    return data


def solve(instructions):
    position, depth, = 0, 0
    aim = 0

    for direction, distance in instructions:
        if direction == 'forward':
            depth += aim * distance
            position += distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance

    return position * depth


if __name__ == '__main__':

    EXPECTED = 900
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
