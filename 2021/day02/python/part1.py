def parse(file):
    with open(file, 'r') as f:
        data = [(dir_, int(dist)) for dir_, dist in
                [line.split() for line in f.read().splitlines()]]
    return data


def solve(instructions):
    position, depth, = 0, 0

    for direction, distance in instructions:
        if direction == 'forward':
            position += distance
        elif direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance

    return position * depth


if __name__ == '__main__':

    EXPECTED = 150
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
