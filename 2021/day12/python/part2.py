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
    def dfs(current, end, visited, used_double=False):
        visited = visited | {current}

        if current == end:
            return 1

        total = 0
        for cave in graph[current]:
            new_double = used_double
            if cave.islower() and cave in visited:
                if used_double or cave == 'start' or cave == 'end':
                    continue
                else:
                    new_double = True

            total += dfs(cave, end, visited, new_double)

        return total

    return dfs('start', 'end', set())


if __name__ == '__main__':

    EXPECTED = 3509
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
