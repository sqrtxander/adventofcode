def solve(file):
    def get_length(substr):
        i = 0
        total_length = 0
        while i < len(substr):
            if substr[i] == '(':
                end = substr.find(')', i)
                length, repeat = map(int, substr[i+1:end].split('x'))
                total_length += get_length(substr[end+1:end+1+length]) * repeat
                i = end + 1 + length
            else:
                total_length += 1
                i += 1
        return total_length

    with open(file, 'r') as f:
        data = f.read()

    return get_length(data)


if __name__ == '__main__':

    EXPECTED = 445
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
