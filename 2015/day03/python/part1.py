if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        directions = f.read()

    houses = set()
    x, y = 0, 0
    for direc in directions:
        houses.add((x, y))

        if direc == '^':
            y += 1
        elif direc == '>':
            x += 1
        elif direc == 'v':
            y -= 1
        elif direc == '<':
            x -= 1

    print(len(houses))