def parse(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def solve(nums):
    gamma = [''] * len(nums[0])
    epsilon = [''] * len(nums[0])

    for i in range(len(nums[0])):
        bits = [num[i] for num in nums]

        if bits.count('1') >= bits.count('0'):
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    return gamma * epsilon


if __name__ == '__main__':

    EXPECTED = 198
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
