def sum_fuel(pos, crabs):
    return sum(abs(num - pos) for num in crabs)


def parse(file):
    with open(file, 'r') as f:
        data = [int(num) for num in f.read().split(',')]
    return data


def solve(crabs):
    fuel_cost = {sum_fuel(i, crabs) for i in range(min(crabs), max(crabs) + 1)}

    return min(fuel_cost)


if __name__ == '__main__':

    EXPECTED = 37
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
