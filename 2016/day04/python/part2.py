import re
from collections import Counter


def solve(file):
    def decrypt(name, sid):
        return ''.join([chr((ord(c) - ord('a') + sid) % 26 + ord('a')) if c != '-' else ' ' for c in name])
    
    with open(file, 'r') as f:
        rooms = [[name, int(sid), checksum] for name, sid, checksum in re.findall(r'([a-z-]+)-(\d+)\[([a-z]+)\]', f.read())]

        real_rooms = {decrypt(name, sid): sid for name, sid, checksum in rooms if checksum == ''.join([k for k, _ in sorted(Counter(name.replace('-', '')).items(), key=lambda x: (-x[1], x[0]))][:5])}
        
        return real_rooms['northpole object storage']
    
if __name__ == '__main__':

    print(solve('../input.in'))
