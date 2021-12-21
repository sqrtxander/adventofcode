def parse(file):
    with open(file, 'r') as f:
        data = [int(num) for num in f.read().split(',')]
    return data


def solve(data, noun=None, verb=None):
    if noun is not None:
        data[1] = noun
    if verb is not None:
        data[2] = verb

    for i in range(0, len(data), 4):
        opcode = data[i]
        read1 = data[i+1]
        read2 = data[i+2]
        store = data[i+3]
        if opcode == 1:
            data[store] = data[read1] + data[read2]
        elif opcode == 2:
            data[store] = data[read1] * data[read2]
        elif opcode == 99:
            break
    return data[0]


if __name__ == '__main__':

    EXPECTED = 3500
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in'), 12, 2))
