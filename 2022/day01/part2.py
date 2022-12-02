def solve(file):
    with open(file, 'r') as f:
        calories = [sum(int(elf_cal) for elf_cal in line.splitlines())
                    for line in f.read().split('\n\n')]

    calories.sort()
    return sum(calories[-3:])


if __name__ == '__main__':

    EXPECTED = 45000
    test = solve('test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('input.in'))
