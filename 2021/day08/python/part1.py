def parse(file):
    with open(file, 'r') as f:
        data = [[x.split() for x in line.split(' | ')] for line in f.read().splitlines()]
    return data


def solve(data):
    count = 0
    for _, output in data:
        for num in output:
            if len(num) in (2, 4, 3, 7):
                count += 1

    return count


if __name__ == '__main__':

    EXPECTED = 26
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
