if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        depths = [int(x) for x in f.readlines()]

    count = sum(depths[i] > depths[i-3] for i in range(3, len(depths)))
    print(count)
