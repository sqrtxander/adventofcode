import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 36
TEST_INPUT = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
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

    body = [[0, 0] for _ in range(10)]

    tail_visited = set()
    tail_visited.add((body[-1][0], body[-1][1]))

    for direc, dist in moves:
        dist = int(dist)
        dx, dy = direcs[direc]
        for _ in range(dist):
            body[0][0] += dx
            body[0][1] += dy

            for i in range(1, len(body)):
                body[i][0], body[i][1] = move_tail(
                    body[i-1][0], body[i-1][1], body[i][0], body[i][1])
            tail_visited.add((body[-1][0], body[-1][1]))

    return len(tail_visited)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
