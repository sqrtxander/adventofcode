import itertools

locations = set()
distances = dict()

with open('inputs/input09.txt', 'r') as f:
    for line in f.readlines():
        # print(line)
        loc1, _, loc2, _, dist = line.split()
        locations.add(loc1)
        locations.add(loc2)
        distances[(loc1, loc2)] = int(dist)
        distances[(loc2, loc1)] = int(dist)

all_distances = []
for path in itertools.permutations(locations):
    # print(path)
    dist = 0
    for i in range(len(path)-1):
        dist += distances[(path[i], path[i + 1])]
    all_distances.append(dist)

print(min(all_distances))
print(max(all_distances))
