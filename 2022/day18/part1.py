import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 64
TEST_INPUT = '''\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''


def get_neighbours(x, y, z):
    yield x+1, y, z
    yield x-1, y, z
    yield x, y+1, z
    yield x, y-1, z
    yield x, y, z+1
    yield x, y, z-1


def solve(inp):
    todo = [tuple(int(num) for num in line.split(','))
            for line in inp.strip().splitlines()]

    done = set()
    area = 0
    while todo:
        curr = todo.pop()
        area += 6
        area -= 2 * \
            sum(neighbour in done for neighbour in get_neighbours(*curr))
        done.add(curr)

    return area


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
