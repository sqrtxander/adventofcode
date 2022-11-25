import re


def solve(file):    
    def replace_nth(string, sub, replace, n):
        find = string.find(sub)
        i = find != -1
        while find != -1 and i != n:
            find = string.find(sub, find + 1)
            i += 1
        if i == n:
            return string[:find] + replace + string[find + len(sub):]
        return string

    with open(file, 'r') as f:
        replacements = re.findall(r'(\w+) => (\w+)', f.read())
        f.seek(0)
        molecule = f.readlines()[-1]

    valid = set()
    for x, y in replacements:
        count = molecule.count(x)
        for i in range(1, count + 1):
            new = replace_nth(molecule, x, y, i)
            valid.add(new)

    return len(valid)
    


if __name__ == '__main__':

    EXPECTED = 7
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
