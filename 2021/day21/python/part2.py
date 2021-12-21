def move_pawn(start, dice):
    return (start + dice - 1) % 10 + 1


def parse(file):
    with open(file, 'r') as f:
        f = f.read().splitlines()
        p1 = int(f[0].split()[-1])
        p2 = int(f[1].split()[-1])

    return p1, p2


def solve(p1, p2):
    # not sure
    return p1, p2


if __name__ == '__main__':

    EXPECTED = 444356092776315
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))
