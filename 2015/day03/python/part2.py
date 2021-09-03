if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        directions = f.read()

    x, y = [0, 0], [0, 0]  # [santa, robot] [santa, robot]
    houses = set()
    person = 0
    for direc in directions:
        houses.add((x[person], y[person]))

        if direc == '^':
            y[person] += 1
        elif direc == '>':
            x[person] += 1
        elif direc == 'v':
            y[person] -= 1
        elif direc == '<':
            x[person] -= 1

        person += 1
        person %= 2

    print(len(houses))