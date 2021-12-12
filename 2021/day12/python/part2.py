from collections import defaultdict


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


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        graph = defaultdict(list)
        for line in f.read().splitlines():
            a, b = line.split('-')
            graph[a].append(b)
            graph[b].append(a)

    print(dfs('start', 'end', set()))
