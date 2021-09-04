import itertools

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        sizes = [int(x) for x in f.readlines()]

    valid = []
    for i in range(1, len(sizes)+1):
        valid += [s for s in itertools.combinations(sizes, i) if sum(s) == 150]
        if len(valid) > 0:
            break

    print(len(valid))
