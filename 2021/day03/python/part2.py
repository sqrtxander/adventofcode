def parse(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def solve(nums):
    o2 = nums.copy()
    co2 = nums.copy()

    for i in range(len(o2[0])):
        bits = [num[i] for num in o2]

        if len(o2) > 1:
            if bits.count('1') >= bits.count('0'):
                o2 = [n for n in o2 if n[i] == '1']
            else:
                o2 = [n for n in o2 if n[i] == '0']

    for i in range(len(co2[0])):
        bits = [num[i] for num in co2]

        if len(co2) > 1:
            if bits.count('1') >= bits.count('0'):
                co2 = [n for n in co2 if n[i] == '0']
            else:
                co2 = [n for n in co2 if n[i] == '1']

    o2 = int(o2[0], 2)
    co2 = int(co2[0], 2)

    return o2*co2


if __name__ == '__main__':

    EXPECTED = 230
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
