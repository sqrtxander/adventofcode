import itertools

if __name__ == '__main__':

    locations = set()
    distances = dict()
    with open('../input.txt', 'r') as f:
        for line in f.readlines():
            loc1, _, loc2, _, dist = line.split()
            locations.add(loc1)
            locations.add(loc2)
            distances[(loc1, loc2)] = int(dist)
            distances[(loc2, loc1)] = int(dist)

    all_distances = set()
    for path in itertools.permutations(locations):
        dist = 0
        for i in range(len(path)-1):
            dist += distances[(path[i], path[i + 1])]
        all_distances.add(dist)

    print(min(all_distances))
