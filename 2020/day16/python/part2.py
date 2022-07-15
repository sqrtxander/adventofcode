import re
from turtle import position


def solve(file):
    def is_valid(value, field):
        _, (l1, u1), (l2, u2) = field
        if l1 <= value <= u1 or l2 <= value <= u2:
            return True
        return False

    def is_valid_all(ticket, fields):
        for value in ticket:
            # breakpoint()
            if not any(is_valid(value, field) for field in fields):
                return False
        return True

    with open(file, 'r') as f:
        data = f.read().split('\n\n')

        fields = [(name, (int(l1), int(u1)), (int(l2), int(u2))) for name, l1, u1, l2, u2 in re.findall(r'([\w +]+): (\d+)-(\d+) or (\d+)-(\d+)', data[0])]
        
        my_ticket = [int(x) for x in data[1].split('\n')[1].split(',')]

        nearby_tickets = [tuple(map(int, num)) for num in [line.split(',') for line in data[2].split('\n')[1:]]]

    valid = [ticket for ticket in nearby_tickets if is_valid_all(ticket, fields)]

    positions = [[] for _ in range(len(valid[0]))]
    for ticket in valid:
        for i in range(len(ticket)):
            positions[i].append(ticket[i])

    product = 1
    remaining_i = [i for i in range(len(positions))]

    while remaining_i:
        for field in fields:
            candidates = [i for i in remaining_i if all(is_valid(value, field) for value in positions[i])]

            if len(candidates) == 1:
                remaining_i.remove(candidates[0])

                if field[0].startswith('departure'):
                    product *= my_ticket[candidates[0]]
                continue            

    return product


if __name__ == '__main__':

    print(solve('../input.in'))
