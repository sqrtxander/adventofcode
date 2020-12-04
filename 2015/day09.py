data = [line.split(' = ') for line in open('inputs/input09.txt').read().strip().split('\n')]
print(data)
for x in range(len(data)):
    data[x][0] = data[x][0].split(' to ')
    data[x][1] = int(data[x][1])
print(data)
