import re
import itertools
import math


def circular_permutations(iterator):
    return list(itertools.permutations(iterator))[:math.factorial(len(iterator)-1)]


if __name__ == '__main__':
    happiness = {}
    people = set()
    with open('../input.txt', 'r') as f:
        for line in f:
            p1, pm, h, p2 = re.findall(r'(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).', line)[0]

            happiness[(p1, p2)] = int(h) if pm == 'gain' else -1 * int(h)
            people.add(p1)

    optimal_score = 0
    for layout in circular_permutations(people):
        score = 0
        for i in range(len(layout)):
            p1 = layout[i]
            p2 = layout[i-1]
            score += happiness[(p1, p2)]
            score += happiness[(p2, p1)]

        if score > optimal_score:
            optimal_score = score

    print(optimal_score)