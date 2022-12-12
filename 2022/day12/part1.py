import os
import heapq
from collections import defaultdict


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 31
TEST_INPUT = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''


def solve(inp):
    def is_valid(source, dest):
        return dest in heightmap and ord(heightmap[source]) + 1 >= ord(heightmap[dest])

    def get_neighbours(x, y):
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if is_valid((x, y), (x+dx, y+dy)):
                yield x + dx, y + dy

    def dijkstra(graph, source, target):
        path_lengths = {v: float('inf') for v in graph}
        path_lengths[source] = 0

        visited = set()
        pq = [(0,) + source]
        heapq.heapify(pq)
        path_lengths = defaultdict(int)
        while pq:
            c, x, y = heapq.heappop(pq)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            path_lengths[(x, y)] = c

            if (x, y) == target:
                return c

            for nx, ny in get_neighbours(x, y):
                heapq.heappush(pq, (c + 1, nx, ny))

    heightmap = {}
    for y, line in enumerate(inp.strip().splitlines()):
        for x, char in enumerate(line):
            heightmap[(x, y)] = char
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)

    heightmap[end] = 'z'
    heightmap[start] = 'a'
    return dijkstra(heightmap, start, end)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
