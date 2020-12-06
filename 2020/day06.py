data = [line.split('\n') for line in open('inputs/input06.txt').read().strip().split('\n\n')]

count_union = 0
count_intersection = 0

for group in data:
    answers_intersection = group[0]
    for person in group:
        answers_intersection = set(answers_intersection) & set(person)
        answers_union = set(''.join(group))

    count_union += len(answers_union)
    count_intersection += len(answers_intersection)

print(f'Part 1: {count_union}')
print(f'Part 2: {count_intersection}')
