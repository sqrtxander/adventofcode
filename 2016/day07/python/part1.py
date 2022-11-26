import re


def solve(file):
    with open(file, 'r') as f:
        ips = f.read().splitlines()

    return sum(bool(re.search(r'(\w)(?!\1)(\w)\2\1', ip)) and not bool(re.search(r'\[\w*(\w)(?!\1)(\w)\2\1\w*\]', ip)) for ip in ips)


if __name__ == '__main__':

    print(solve('../input.in'))
