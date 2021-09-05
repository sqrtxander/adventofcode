import re


def replace_nth(string, sub, replace, n):
    find = string.find(sub)
    i = find != -1
    while find != -1 and i != n:
        find = string.find(sub, find + 1)
        i += 1
    if i == n:
        return string[:find] + replace + string[find + len(sub):]
    return string


def next_iteration(molecule, depth=1):
    molecules = set()
    for x, y in replacements:
        for i in range(1, molecule.count(y) + 1):
            new = replace_nth(molecule, y, x, i)
            if new not in starters:
                molecules.add(new)
            else:
                print('SUCCESS')
                print(depth+1)
                exit()
    for mol in molecules:
        next_iteration(mol, depth+1)


def part_2(molecule, replacements):
    depth = 1
    while molecule not in starters:
        for reactant, product in replacements:
            if product in molecule:
                molecule = molecule.replace(product, reactant)
                print(molecule)
                depth += 1

    return depth


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        replacements = re.findall(r'(\w+) => (\w+)', f.read())
        f.seek(0)
        molecule = f.readlines()[-1]
        # molecule = 'HOHOHO'
        starters = [x[1] for x in replacements if x[0] == 'e']
        replacements = [x for x in replacements if x[0] != 'e']

    print(part_2(molecule, replacements))
    # print(next_iteration(molecule))

    # unsure how to continue
