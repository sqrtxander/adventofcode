def solve(file):
    with open(file, 'r') as f:
        data = f.read()

    i = 0
    total_length = 0
    while i < len(data):
        if data[i] == '(':
            end = data.find(')', i)
            length, repeat = map(int, data[i+1:end].split('x'))
            total_length += len(data[end+1:end+1+length]) * repeat
            i = end + 1 + length
        else:
            total_length += 1
            i += 1

    return total_length


if __name__ == '__main__':

    EXPECTED = 238
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
