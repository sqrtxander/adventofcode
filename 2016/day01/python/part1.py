def solve(file):
    with open(file, 'r') as f:
        instructions = [(line[0], int(line[1:])) for line in f.read().split(', ')]

    x, y = 0, 0
    direction = 1j

    for turn, distance in instructions:
        if turn == 'L':
            direction *= 1j
        elif turn == 'R':
            direction *= -1j
        x += distance * direction.real
        y += distance * direction.imag

    return int(abs(x) + abs(y))

if __name__ == '__main__':

    EXPECTED = 8
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
