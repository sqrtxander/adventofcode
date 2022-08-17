def solve(file):
    with open(file, 'r') as f:
        answers = [line.split('\n') for line in f.read().split('\n\n')]

    count = 0
    for group in answers:
        intersect = set(group[0])
        for person in group[1:]:
            intersect = intersect & set(person)
        count += len(intersect)
    return count


if __name__ == '__main__':

    EXPECTED = 6
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
