def solve(file):
    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]
    
    seat_ids = []

    for seat in data:
        row = int(seat[:7].replace('B', '1').replace('F', '0'), 2)
        col = int(seat[-3:].replace('R', '1').replace('L', '0'), 2)
        seat_ids.append(row * 8 + col)

    return max(seat_ids)

if __name__ == '__main__':

    EXPECTED = 820
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
