import re
from collections import Counter


def solve(file):
    with open(file, 'r') as f:
        rooms = [[Counter(name.replace('-', '')), int(sid), checksum] for name, sid, checksum in re.findall(r'([a-z-]+)-(\d+)\[([a-z]+)\]', f.read())]

        
    return sum([sid for name, sid, checksum in rooms if checksum == ''.join([k for k, _ in sorted(name.items(), key=lambda x: (-x[1], x[0]))][:5])])


if __name__ == '__main__':

    print(solve('../input.in'))
