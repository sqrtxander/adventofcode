import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 24000
TEST_INPUT = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''


def solve(inp):
    calories = [sum(int(elf_cal) for elf_cal in line.splitlines())
                for line in inp.strip().split('\n\n')]

    return max(calories)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
