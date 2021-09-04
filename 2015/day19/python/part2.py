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


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        replacements = re.findall(r'(\w+) => (\w+)', f.read())
        f.seek(0)
        molecule = f.readlines()[-1]

    # unsure how to continue
