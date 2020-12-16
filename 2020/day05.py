data = [line.strip() for line in open('inputs/input05.txt').readlines()]

seat_ids = []

for seat in data:
    row = int(seat[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(seat[-3:].replace('R', '1').replace('L', '0'), 2)
    seat_ids.append(row * 8 + col)

print(f'Part 1: {max(seat_ids)}')
my_seat = [x for x in range(min(seat_ids), max(seat_ids)) if x not in seat_ids and x+1 in seat_ids and x-1 in seat_ids]
print(f'Part 2: {my_seat[0]}')
