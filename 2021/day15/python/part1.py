import heapq
from collections import defaultdict


def get_neighbours(x, y, width, height):
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if x + dx < 0 or x + dx >= width:
            continue
        if y + dy < 0 or y + dy >= height:
            continue
        yield x + dx, y + dy


def dijkstra(graph, width, height, source, target):
    path_lengths = {v: float('inf') for v in graph}
    path_lengths[source] = 0

    visited = set()
    pq = [(0,) + source]
    heapq.heapify(pq)
    path_lengths = defaultdict(int)
    while len(pq) > 0:
        c, x, y = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        path_lengths[(x, y)] = c

        if (x, y) == target:
            return c

        for nx, ny in get_neighbours(x, y, width, height):
            heapq.heappush(pq, (c + graph[(nx, ny)], nx, ny))


def parse(file):
    with open(file, 'r') as f:
        f = f.read().splitlines()
        height = len(f)
        width = len(f[0])
        graph = {}
        for y, line in enumerate(f):
            for x, n in enumerate(line):
                graph[(x, y)] = int(n)

    return height, width, graph


def solve(height, width, graph):
    return dijkstra(graph, width, height, (0, 0), (width-1, height-1))


if __name__ == '__main__':

    EXPECTED = 40
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))

