if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [(dir_, int(dist)) for dir_, dist in [line.split() for line in f.read().splitlines()]]

    position, depth, = 0, 0

    for direction, distance in data:
        if direction == 'forward':
            position += distance
        elif direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance

    print(position*depth)
