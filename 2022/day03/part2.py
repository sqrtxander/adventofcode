

import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 70
TEST_INPUT = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''


def solve(inp):
    def common_letter(str1, str2, str3):
        return set(str1).intersection(str2).intersection(str3).pop()

    rucksacks = [line for line in inp.strip().splitlines()]

    total_priorities = 0

    for i in range(0, len(rucksacks), 3):
        badge = common_letter(rucksacks[i], rucksacks[i+1], rucksacks[i+2])
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
