from collections import defaultdict

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [[tuple(map(int, num.split(','))) for num in line.split(' -> ')]
                for line in f.read().splitlines()]

    lines = defaultdict(lambda: 0)

    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1

            for y in range(y1, y2 + 1):
                lines[(x1, y)] += 1

        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1

            for x in range(x1, x2 + 1):
                lines[(x, y1)] += 1

    print(sum(x > 1 for x in lines.values()))
