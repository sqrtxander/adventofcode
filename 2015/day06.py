import numpy as np

data = [x.split(' through ') for x in open('inputs/input06.txt').read().strip().split('\n')]

for i in range(len(data)):
    data[i][0] = data[i][0].split(' ')
    data[i][1] = [int(x) for x in data[i][1].split(',')]

for i in range(len(data)):
    j = [int(x) for x in data[i][0][-1].split(',')]
    del data[i][0][-1]
    data[i].insert(1, j)
    data[i][0] = ''.join(data[i][0])


# data = [['turnoff', [998, 998], [999, 999]], ['turnon', [0, 0], [999, 999]], ['turnoff', [0, 0], [2, 2]], ['toggle', [0, 0], [999, 999]]]
# data = [['toggle', [0, 3], [1, 4]]]


lights = np.zeros((1000, 1000), dtype=np.bool)
brightness = np.zeros((1000, 1000), dtype=np.int)
for instruction, [x1, y1], [x2, y2] in data:

    if instruction == 'turnon':
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[j][i] = True
                brightness[j][i] += 1

    elif instruction == 'turnoff':
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[j][i] = False
                brightness[j][i] -= 1
                if brightness[j][i] < 0:
                    brightness[j][i] = 0

    elif instruction == 'toggle':
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights[j][i] = not(lights[j][i])
                brightness[j][i] += 2

print(f'Part 1: {int(np.sum(lights))}')
print(f'Part 2: {int(np.sum(brightness))}')
