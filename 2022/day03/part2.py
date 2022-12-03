def solve(file):
    def common_letter(str1, str2, str3):
        return set(str1).intersection(str2).intersection(str3).pop()

    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]

    total_priorities = 0 

    for i in range(0, len(data), 3):
        badge = common_letter(data[i], data[i+1], data[i+2])
        if badge.islower():
            total_priorities += ord(badge) - 96
        else:
            total_priorities +=  ord(badge) - 38

    return total_priorities

if __name__ == '__main__':

    EXPECTED = 70
    test = solve('test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('input.in'))
