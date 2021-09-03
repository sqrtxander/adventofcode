if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        dimensions = [list(map(int, x.split('x'))) for x in f.readlines()]

    ribbon = 0
    for dim in dimensions:
        dim.sort()
        l, w, h = dim
        ribbon += (2*(l + w) + l*w*h)

    print(ribbon)