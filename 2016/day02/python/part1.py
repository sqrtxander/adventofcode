def solve(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()

    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    x, y = 1, 1
    code = ''

    for line in data:
        for char in line:
            if char == 'U' and y > 0:
                y -= 1
            elif char == 'D' and y < 2:
                y += 1
            elif char == 'L' and x > 0:
                x -= 1
            elif char == 'R' and x < 2:
                x += 1
        code += keypad[y][x]

    return code

if __name__ == '__main__':

    EXPECTED = '1985'
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
