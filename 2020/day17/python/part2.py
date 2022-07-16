from collections import defaultdict


def solve(file):
    def get_neighbours(coords):
        x, y, z, w = coords
        neighbours = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    for l in (-1, 0, 1):
                        if i == 0 and j == 0 and k == 0 and l == 0:
                            continue
                        neighbours.append((x + i, y + j, z + k, w + l))
        return neighbours

    with open(file, 'r') as f:
        data = f.read().splitlines() 
        cubes = defaultdict(int)

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == '#':
                    cubes[(x, y, 0, 0)] = 1

    for _ in range(6):
        new_cubes = defaultdict(int)

        x0 = min(coords[0] for coords in cubes) - 1
        x1 = max(coords[0] for coords in cubes) + 1
        y0 = min(coords[1] for coords in cubes) - 1
        y1 = max(coords[1] for coords in cubes) + 1
        z0 = min(coords[2] for coords in cubes) - 1
        z1 = max(coords[2] for coords in cubes) + 1
        w0 = min(coords[3] for coords in cubes) - 1
        w1 = max(coords[3] for coords in cubes) + 1

        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    for w in range(w0, w1 + 1):
                        neighbours = get_neighbours((x, y, z, w))
                        count = sum(cubes[n] for n in neighbours)
                        if cubes[(x, y, z, w)]:
                            if count == 2 or count == 3:
                                new_cubes[(x, y, z, w)] = 1
                            else:
                                new_cubes[(x, y, z, w)] = 0
                        else:
                            if count == 3:
                                new_cubes[(x, y, z, w)] = 1
                            else:
                                new_cubes[(x, y, z, w)] = 0

        cubes = new_cubes.copy()

    return sum(cubes.values())

if __name__ == '__main__':

    EXPECTED = 848
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
