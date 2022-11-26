import re


def solve(file):
    with open(file, 'r') as f:
        ips = f.read().splitlines()

    return sum(bool(re.search(r'(\w)(?!\1)(\w)\1\w*(?:\[\w*]\w*)*?\[\w*?\2\1\2|(\w)(?!\3)(\w)\3\w*](?:\w*\[\w*])*?\w*?\4\3\4', ip)) for ip in ips)


if __name__ == '__main__':

    print(solve('../input.in'))
