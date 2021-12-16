def parse(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def solve(subsystem):
    reverse = {')': '(', ']': '[', '}': '{', '>': '<'}
    closing = (')', ']', '}', '>')
    point_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points = 0

    for line in subsystem:
        characters = [line[0]]
        for char in line[1:]:
            if char in closing:
                if reverse[char] == characters[-1]:
                    characters.pop(-1)
                else:
                    points += point_map[char]
                    break
            else:
                characters.append(char)

    return points


if __name__ == '__main__':

    EXPECTED = 26397
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
