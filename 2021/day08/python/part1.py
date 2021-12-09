if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [[x.split() for x in line.split(' | ')] for line in f.read().splitlines()]

    count = 0
    for _, output in data:
        for num in output:
            if len(num) in (2, 4, 3, 7):
                count += 1

    print(count)
