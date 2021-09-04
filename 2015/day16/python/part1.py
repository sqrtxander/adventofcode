import re


def valid_sue(condition, properties):
    for prop in properties:
        if properties[prop] != condition[prop]:
            return False
    return True


if __name__ == '__main__':
    sues = []
    with open('../input.txt', 'r') as f:
        for line in f:
            a, an, b, bn, c, cn = re.findall(r'Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)[0]
            sues.append({a: int(an), b: int(bn), c: int(cn)})

    condition = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    for i in range(len(sues)):
        if valid_sue(condition, sues[i]):
            print(i + 1)
            break
