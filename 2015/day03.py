data = list(open('inputs/input03.txt').read())

houses = []
x, y = 0, 0
for direction in data:
    if (x, y) not in houses:
        houses.append((x, y))

    if direction == '^':
        y += 1
    elif direction == '>':
        x += 1
    elif direction == 'v':
        y -= 1
    elif direction == '<':
        x -= 1

print(f'part 1: {len(houses)}')

x, y = [0, 0], [0, 0] # [santa, robot] [santa, robot]
houses = []
person = 0
for direction in data:
    
    if (x[person], y[person]) not in houses:
        houses.append((x[person], y[person]))

    if direction == '^':
        y[person] += 1
    elif direction == '>':
        x[person] += 1
    elif direction == 'v':
        y[person] -= 1
    elif direction == '<':
        x[person] -= 1

    person += 1
    person %= 2

print(f'Part 2: {len(houses)}')
