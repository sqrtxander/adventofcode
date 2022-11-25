import re


def solve(file):
    def replace(x):
        return replacements[x.group()]

    with open(file, 'r') as f:
        replacements = re.findall(r'(\w+) => (\w+)', f.read())
        f.seek(0)
        molecule = f.readlines()[-1][::-1]
        replacements = {x[1][::-1]: x[0][::-1] for x in replacements}


    count = 0
    while molecule not in ('e', 'ee'):
        molecule = re.sub('|'.join(replacements.keys()), replace, molecule, 1)
        # print(molecule)
        count += 1

    return count



if __name__ == '__main__':

    EXPECTED = 6
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print('solved test case')
    print(solve('../input.in'))
