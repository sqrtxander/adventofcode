data = [line.split(' -> ') for line in open('inputs/input07.txt').read().strip().split('\n')]
print(data)
for line in range(len(data)):
    data[line][0] = data[line][0].split(' ')

print(data)

# if
