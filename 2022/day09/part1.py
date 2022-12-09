import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 13
TEST_INPUT = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''


def solve(inp):
    def move_tail(headx, heady, tailx, taily):
        dx = headx - tailx
        dy = heady - taily
        manhattan = abs(dx) + abs(dy)

        if manhattan >= 3:
            tailx += dx // abs(dx)
            taily += dy // abs(dy)

        elif abs(dx) > 1:
            tailx += dx // abs(dx)
        elif abs(dy) > 1:
            taily += dy // abs(dy)

        return tailx, taily

    moves = [(direc, int(dist)) for direc, dist in (line.split(' ')
                                                    for line in inp.strip().splitlines())]

    direcs = {'U': (0, -1),
              'D': (0, 1),
              'L': (-1, 0),
              'R': (1, 0)}

    headx, heady = 0, 0
    tailx, taily = 0, 0

    tail_visited = set()
    tail_visited.add((tailx, taily))
    for direc, dist in moves:
        dx, dy = direcs[direc]
        for _ in range(dist):
            headx += dx
            heady += dy
            tailx, taily = move_tail(headx, heady, tailx, taily)
            tail_visited.add((tailx, taily))

    return len(tail_visited)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
