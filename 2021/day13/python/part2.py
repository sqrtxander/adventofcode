from itertools import groupby


def print_paper(coords):
    unzipped_coords = list(zip(*coords))
    max_x = max(unzipped_coords[0])
    max_y = max(unzipped_coords[1])

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if [x, y] in coords:
                print('██', end='')
            else:
                print('  ', end='')
        print()


def parse(file):
    with open(file, 'r') as f:
        coords, folds = f.read().split('\n\n')

        coords = [[int(num) for num in line.split(',')] for line in coords.split('\n')]

        folds = folds.split('\n')
        for i, fold in enumerate(folds):
            fold = fold.split(' ')[-1]
            axis, val = fold.split('=')
            folds[i] = axis, int(val)

    return coords, folds


def solve(coords, folds):
    for (axis, val) in folds:
        if axis == 'x':
            for i, (x, y) in enumerate(coords):
                if x > val:
                    coords[i] = [2 * val - x, y]
        elif axis == 'y':
            for i, (x, y) in enumerate(coords):
                if y > val:
                    coords[i] = [x, 2 * val - y]

        coords.sort()
        coords = list(x for x, _ in groupby(coords))

    print_paper(coords)


if __name__ == '__main__':

    solve(*parse('../input.in'))
