from collections import defaultdict


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


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        graph = defaultdict(list)
        for line in f.read().splitlines():
            a, b = line.split('-')
            graph[a].append(b)
            graph[b].append(a)

    print(dfs('start', 'end', set()))
