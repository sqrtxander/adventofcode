def solve(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()

    keypad = [[None, None, '1', None, None],
              [None, '2', '3', '4', None],
              ['5', '6', '7', '8', '9'],
              [None, 'A', 'B', 'C', None],
              [None, None, 'D', None, None]]

    x, y = 0, 3
    code = ''

    for line in data:
        for char in line:
            if char == 'U' and y > 0 and keypad[y - 1][x] is not None:
                y -= 1
            elif char == 'D' and y < 4 and keypad[y + 1][x] is not None:
                y += 1
            elif char == 'L' and x > 0 and keypad[y][x - 1] is not None:
                x -= 1
            elif char == 'R' and x < 4 and keypad[y][x + 1] is not None:
                x += 1
        code += keypad[y][x]

    return code

if __name__ == '__main__':

    EXPECTED = '5DB3'
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
