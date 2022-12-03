def solve(file):
    def common_letter(str1, str2):
        return set(str1).intersection(str2).pop() 

    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]

    total_priorities = 0 

    for line in data:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        badge = common_letter(first_half, second_half)
        if badge.islower():          
            total_priorities += ord(badge) - 96
        else:
            total_priorities +=  ord(badge) - 38    

    return total_priorities


if __name__ == '__main__':

    EXPECTED = 157
    test = solve('test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('input.in'))
