if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [(dir_, int(dist)) for dir_, dist in
                [line.split() for line in f.read().splitlines()]]

    position, depth, = 0, 0
    aim = 0

    for direction, distance in data:
        if direction == 'forward':
            depth += aim * distance
            position += distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance

    print(position*depth)
