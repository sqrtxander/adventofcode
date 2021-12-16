from collections import defaultdict


def parse(file):
    with open(file, 'r') as f:
        graph = defaultdict(list)
        for line in f.read().splitlines():
            a, b = line.split('-')
            graph[a].append(b)
            graph[b].append(a)
    return graph


def solve(graph):
    def dfs(current, end, visited):
        if current in visited and current.islower():
            return 0

        visited = visited | {current}

        if current == end:
            return 1

        total = 0
        for cave in graph[current]:
            total += dfs(cave, end, visited)

        return total

    return dfs('start', 'end', set())


if __name__ == '__main__':

    EXPECTED = 226
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
