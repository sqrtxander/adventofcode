if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        depths = [int(x) for x in f.readlines()]

    count = sum(depths[i] > depths[i-1] for i in range(1, len(depths)))
    print(count)
