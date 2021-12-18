def parse(file):
    with open(file, 'r') as f:
        _, _, x, y = f.read().split(' ')
        x = x[2:-1]
        y = y[2:]

        x1, x2 = (int(num) for num in x.split('..'))
        y1, y2 = (int(num) for num in y.split('..'))

    return x1, x2, y1, y2


def solve(y1):
    vy = abs(y1) - 1
    return (vy + 1) * vy // 2


if __name__ == '__main__':
    EXPECTED = 45
    test = solve(parse('../test.in')[2])
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')[2]))
