import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 157
TEST_INPUT = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''


def solve(inp):
    def common_letter(str1, str2):
        return set(str1).intersection(str2).pop()

    data = [line for line in inp.strip().splitlines()]

    total_priorities = 0

    for line in data:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        badge = common_letter(first_half, second_half)
        if badge.islower():
            total_priorities += ord(badge) - 96
        else:
            total_priorities += ord(badge) - 38

    return total_priorities


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
