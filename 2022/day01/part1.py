def solve(file):
    with open(file, 'r') as f:
        calories = [sum(int(elf_cal) for elf_cal in line.splitlines())
                    for line in f.read().split('\n\n')]

    return max(calories)


if __name__ == '__main__':

    EXPECTED = 24000
    test = solve('test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('input.in'))
