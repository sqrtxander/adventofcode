data = [x.split('x') for x in open('inputs/input02.txt').read().strip().split('\n')]

for x in range(len(data)):
    for y in range(len(data[x])):
        data[x][y] = int(data[x][y])


paper = 0
ribbon = 0
for l, w, h, in data:
    min_side = min([l * w, l * h, w * h])
    paper += 2 * (l * w + l * h + w * h) + min_side
    min_perim = min([2 * (l + w), 2 * (l + h), 2 * (w + h)])
    ribbon += l * w * h + min_perim

print(f'Part 1: {paper}')
print(f'Part 2: {ribbon}')
