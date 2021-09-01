import re
import itertools
import math


def circular_permutations(iterator):
    return list(itertools.permutations(iterator))[:math.factorial(len(iterator)-1)]


happiness = {}
people = set()
with open('inputs/input13.txt', 'r') as f:
    for line in f:
        p1, pm, h, p2 = re.findall(r'(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).', line)[0]

        happiness[(p1, p2)] = int(h) if pm == 'gain' else -1 * int(h)
        people.add(p1)

scores = []
optimal = None
for layout in circular_permutations(people):
    score = 0
    for i in range(len(layout)):
        p1 = layout[i]
        p2 = layout[i-1]
        score += happiness[(p1, p2)]
        score += happiness[(p2, p1)]

    scores.append(score)

    if score == max(scores):
        optimal = layout

print(max(scores))

scores = []
for i in range(len(optimal)):
    score = 0
    for j in range(len(optimal)):
        p1 = optimal[j]
        p2 = optimal[j-1]
        score += happiness[(p1, p2)] if j != i else 0
        score += happiness[(p2, p1)] if j != i else 0
    scores.append(score)

print(max(scores))