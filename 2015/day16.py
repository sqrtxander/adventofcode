import re


def valid_sue(condition, properties):
    for prop in properties:
        if properties[prop] != condition[prop]:
            return False
    return True


def valid_sue_2(condition, properties):
    for prop in properties:
        if prop in ('cats', 'trees'):
            if properties[prop] <= condition[prop]:
                return False
        elif prop in('pomeranians', 'goldfish'):
            if properties[prop] >= condition[prop]:
                return False
        else:
            if properties[prop] != condition[prop]:
                return False
    return True


sues = []
with open('inputs/input16.txt', 'r') as f:
    for line in f:
        a, an, b, bn, c, cn = re.findall(r'Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)[0]
        sues.append({a: int(an), b: int(bn), c: int(cn)})

condition = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for i in range(len(sues)):
    if valid_sue(condition, sues[i]):
        print(i + 1)
        break

for i in range(len(sues)):
    if valid_sue_2(condition, sues[i]):
        print(i + 1)
        break

