data = [0] + [int(x) for x in open('inputs/input10.txt').readlines()]
data.sort()
data.append(data[-1]+3) # add final adapter

differences = []
for pos in range(1, len(data)):
    differences.append(data[pos] - data[pos-1])

print(f'Part 1: {differences.count(1)*differences.count(3)}')

ways = [0] * (data[-1] + 1)
ways[0] = 1
for n in data[1:]:
    ways[n] = ways[n - 2] + ways[n - 1] + ways[n - 3]

print(f'Part 2: {ways[-1]}')
