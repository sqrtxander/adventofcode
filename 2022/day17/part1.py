import os
import itertools
from collections import defaultdict, deque

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 3068
TEST_INPUT = '''\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''


class Rock:
    def __init__(self, type_, maxy):
        if type_ == 0:
            self.tiles = [(2, maxy + 4), (3, maxy + 4),
                          (4, maxy + 4), (5, maxy + 4)]
        elif type_ == 1:
            self.tiles = [(2, maxy + 5), (3, maxy + 4),
                          (3, maxy + 5), (3, maxy + 6), (4, maxy + 5)]
        elif type_ == 2:
            self.tiles = [(2, maxy + 4), (3, maxy + 4),
                          (4, maxy + 4), (4, maxy + 5), (4, maxy + 6)]
        elif type_ == 3:
            self.tiles = [(2, maxy + 4), (2, maxy + 5),
                          (2, maxy + 6), (2, maxy + 7)]
        elif type_ == 4:
            self.tiles = [(2, maxy + 4), (3, maxy + 4),
                          (2, maxy + 5), (3, maxy + 5)]

    def has_fallen(self, grid):
        for x, y in self.tiles:
            if grid[(x, y - 1)] or (y - 1) <= 0:
                return True
        return False

    def can_blow(self, grid, dir_):
        for x, y in self.tiles:
            if grid[(x + dir_, y)] or x + dir_ < 0 or x + dir_ > 6:
                return False
        return True

    def move(self, dx, dy):
        self.tiles = [(x + dx, y + dy) for x, y in self.tiles]

    def fall(self, grid):
        if self.has_fallen(grid):
            return False
        self.move(0, -1)
        return True


def print_grid(grid, maxy):
    minx = 0
    maxx = 6
    miny = 1
    for y in range(7 + maxy, miny - 1, -1):
        for x in range(minx, maxx + 1):
            if grid[(x, y)]:
                print('#', end='')
            # elif (x, y) in tiles:
            #     print('@', end='')
            else:
                print('.', end='')
        print()


def solve(inp):
    types = deque([0, 1, 2, 3, 4])
    gusts = deque([1 if dir_ == '>' else -1 for dir_ in inp.strip()])
    grid = defaultdict(bool)
    maxy = 0
    for _ in range(2022):
        type_ = types.popleft()
        types.append(type_)
        rock = Rock(type_, maxy)
        while True:
            gust = gusts.popleft()
            gusts.append(gust)
            if rock.can_blow(grid, gust):
                rock.move(gust, 0)
            if rock.has_fallen(grid):
                break
            rock.move(0, -1)

        maxy = max(maxy, max(y for _, y in rock.tiles))
        for x, y in rock.tiles:
            grid[(x, y)] = True

    return maxy


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
