import re

test = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''


fields = {name: ((int(l1), int(u1)), (int(l2), int(u2))) for name, l1, u1, l2, u2 in re.findall(r'([\w +]+): (\d+)-(\d+) or (\d+)-(\d+)', open('inputs/input16.txt').read())}
nearby_tickets = [tuple(map(int, x)) for x in (line.strip().split(',') for line in open('inputs/input16.txt').readlines()[25:])]
ranges = tuple(x for y in fields.values() for x in y)

# fields = [(int(l), int(u)) for l, u in re.findall(r'(\d+)-(\d+)', test)]
# other_tickets = [line.strip().split(',') for line in test.split('\n')[8:]]

print(nearby_tickets)
print(fields)
print(ranges)

def in_bounds(value):
    return any(l <= value <= u for l, u in ranges)


valid_tickets = []
error_rate = 0
print(error_rate)
for ticket in nearby_tickets:
    check = 0
    for value in ticket:
        if not in_bounds(value):
            error_rate += value
            check += 1
    if check == 0:
        valid_tickets.append(ticket)
print(f'Part 1: {error_rate}')
print(valid_tickets)
print(len(valid_tickets))

print(valid_tickets)
# fields_ans = [list(range(len(valid_tickets[0])))] * len(valid_tickets[0])
#
# for i in range(len(valid_tickets[0])):
#     for ticket in valid_tickets:
#         for c, value in enumerate(ticket):
#             if c not in fields_ans[i]:
#                 break
#             if not all(l <= value <= u for l, u in fields[i//2:i//2+2]):
#                 fields_ans[i].remove(c)
#
#
# print(fields_ans)