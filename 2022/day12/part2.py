import os
import heapq
from collections import defaultdict


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 29
TEST_INPUT = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''


def solve(inp):
    def is_valid(x1, y1, x2, y2):
        return (x2, y2) in heightmap and ord(heightmap[(x1, y1)]) - 1 <= ord(heightmap[(x2, y2)])

    def get_neighbours(x, y):
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if is_valid(x, y, x+dx, y+dy):
                yield x + dx, y + dy

    def dijkstra(graph, source, targets):
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

            if (x, y) in targets:
                return c

            for nx, ny in get_neighbours(x, y):
                heapq.heappush(pq, (c + 1, nx, ny))

    heightmap = {}
    starts = set()
    for y, line in enumerate(inp.strip().splitlines()):
        for x, char in enumerate(line):
            heightmap[(x, y)] = char
            if char == 'a':
                starts.add((x, y))
            elif char == 'S':
                heightmap[(x, y)] = 'a'
                starts.add((x, y))
            elif char == 'E':
                end = (x, y)

    heightmap[end] = 'z'

    return dijkstra(heightmap, end, starts)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
