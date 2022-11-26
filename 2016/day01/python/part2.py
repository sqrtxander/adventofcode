def solve(file):
    with open(file, 'r') as f:
        instructions = [(line[0], int(line[1:])) for line in f.read().split(', ')]

    x, y = 0, 0
    direction = 1j
    visited = set()

    for turn, distance in instructions: 
        if turn == 'L':
            direction *= 1j
        elif turn == 'R':
            direction *= -1j

        for _ in range(distance):
            x += direction.real
            y += direction.imag
            if (x, y) in visited:
                return int(abs(x) + abs(y))
            visited.add((x, y))
        

if __name__ == '__main__':

    EXPECTED = 4
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
