def solve(file):
    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]
    
    seat_ids = []

    for seat in data:
        row = int(seat[:7].replace('B', '1').replace('F', '0'), 2)
        col = int(seat[-3:].replace('R', '1').replace('L', '0'), 2)
        seat_ids.append(row * 8 + col)

    return [x for x in range(min(seat_ids), max(seat_ids)) if x not in seat_ids and x+1 in seat_ids and x-1 in seat_ids][0]
 

if __name__ == '__main__':

    print(solve('../input.in'))
