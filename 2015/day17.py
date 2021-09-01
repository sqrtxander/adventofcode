import itertools

with open('inputs/input17.txt', 'r') as f:
    sizes = [int(x) for x in f.readlines()]


valid = []
for i in range(len(sizes)):
    valid += [s for s in itertools.combinations(sizes, i) if sum(s) == 150]
smallest_valid = [x for x in valid if len(x) == len(valid[0])]

print(len(valid))
print(len(smallest_valid))
