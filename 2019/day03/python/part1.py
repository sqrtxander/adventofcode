def create_plot(wire):
    plot = set()
    x, y = 0, 0
    for cmd in wire:
        for _ in range(int(cmd[1:])):
            if cmd[0] == 'R':
                x += 1
            elif cmd[0] == 'L':
                x -= 1
            elif cmd[0] == 'U':
                y += 1
            elif cmd[0] == 'D':
                y -= 1
            else:
                raise AssertionError
            plot.add((x, y))
    return plot


def parse(file):
    with open(file, 'r') as f:
        data = [cmd.split(',') for cmd in f.read().splitlines()]
    return data


def solve(data):

    wire1 = create_plot(data[0])
    wire2 = create_plot(data[1])
    intersections = wire1.intersection(wire2)
    distances = {abs(x) + abs(y) for x, y in intersections}
    return min(distances)


if __name__ == '__main__':

    EXPECTED = 159
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
