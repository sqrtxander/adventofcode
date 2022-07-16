import heapq
from collections import defaultdict


def solve(file):
    def dijkstra(neighbours, source, target):
        path_lengths = {v: float('inf') for v in neighbours}
        path_lengths[source] = 0

        visited = set()
        pq = [(0, source)]
        heapq.heapify(pq)
        path_lengths = defaultdict(int)
        # breakpoint()
        while len(pq) > 0:
            c, p = heapq.heappop(pq)
            if p in visited:
                continue
            visited.add(p)

            # breakpoint()

            path_lengths[p] = c

            if p == target:
                return c

            for p in neighbours[p]:
                heapq.heappush(pq, (c + 1, p))

    with open(file, 'r') as f:
        # orbits = {b: a for a, b in (line.split(')') for line in f.read().splitlines())}
        graph = {}
        neighbours = defaultdict(list)
        for line in f.read().splitlines():
            a, b = line.split(')')
            graph[a] = 1
            graph[b] = 1
            neighbours[a].append(b)
            neighbours[b].append(a)

    return dijkstra(neighbours, 'SAN', 'YOU') - 2
    
if __name__ == '__main__':

    EXPECTED = 4
    test = solve('../test2.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
