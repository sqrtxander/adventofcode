if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        depths = [int(x) for x in f.readlines()]

    count = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i-3]:
            count += 1

    print(count)
