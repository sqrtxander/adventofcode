from itertools import groupby

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        coords, folds = f.read().split('\n\n')

        coords = [[int(num) for num in line.split(',')] for line in coords.split('\n')]

        folds = folds.split('\n')
        for i, fold in enumerate(folds):
            fold = fold.split(' ')[-1]
            axis, val = fold.split('=')
            folds[i] = axis, int(val)

    axis, val = folds[0]
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
    print(len(coords))
