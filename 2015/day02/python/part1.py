if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        dimensions = [list(map(int, x.split('x'))) for x in f.readlines()]

    paper = 0
    for dim in dimensions:
        dim.sort()
        l, w, h = dim
        paper += (3*l*w + 2*w*h + 2*h*l)

    print(paper)