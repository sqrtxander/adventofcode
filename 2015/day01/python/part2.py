if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        directions = f.read()

    floor = 0
    for i, bracket in enumerate(directions):
        if bracket == '(':
            floor += 1
        elif bracket == ')':
            floor -= 1
        if floor == -1:
            print(i+1)
            break