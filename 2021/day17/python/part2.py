def parse(file):
    with open(file, 'r') as f:
        _, _, x, y = f.read().split(' ')
        x = x[2:-1]
        y = y[2:]

        x1, x2 = (int(num) for num in x.split('..'))
        y1, y2 = (int(num) for num in y.split('..'))

    return x1, x2, y1, y2


def solve(x1, x2, y1, y2):
    total = 0
    for VX in range(1, x2 + 1):
        for VY in range(y1, abs(y1)):
            x, y = 0, 0
            vx, vy = VX, VY
            for _ in range(2 * abs(y1) + 1):
                x += vx
                y += vy
                vx = max(vx - 1, 0)
                vy -= 1
                if x1 <= x <= x2 and y1 <= y <= y2:
                    total += 1
                    break
                elif x > x2 or y < y1:
                    break
    return total


if __name__ == '__main__':
    EXPECTED = 112
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))
