import os
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 'CMZ'
TEST_INPUT = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''


def solve(inp):
    init, moves = inp.split('\n\n')

    towers = [[] for _ in range((len(init.splitlines()[-1]) + 2) // 4)]

    for line in init.splitlines()[:-1]:
        for i, char in enumerate(line):
            if char.isalpha():
                towers[(i+2)//4].append(char)

    for line in moves.splitlines():
        count, from_tower, to_tower = (int(num)
                                       for num in re.findall(r'\d+', line))

        towers[to_tower - 1][:0] = towers[from_tower - 1][:count][::-1]
        towers[from_tower - 1] = towers[from_tower - 1][count:]


    return ''.join(tower[0] for tower in towers)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
