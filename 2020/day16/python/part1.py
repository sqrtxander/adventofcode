import re


def solve(file):
    with open(file, 'r') as f:
        data = f.read().split('\n\n')

        fields = {name: ((int(l1), int(u1)), (int(l2), int(u2))) for name, l1, u1, l2, u2 in re.findall(r'([\w +]+): (\d+)-(\d+) or (\d+)-(\d+)', data[0])}
        
        my_ticket = [int(x) for x in data[1].split('\n')[1].split(',')]

        nearby_tickets = [tuple(map(int, num)) for num in [line.split(',') for line in data[2].split('\n')[1:]]]

        ranges = tuple(x for y in fields.values() for x in y)

    error_rate = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not any(l <= value <= u for l, u in ranges):
                error_rate += value
    return error_rate

if __name__ == '__main__':

    EXPECTED = 71
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
