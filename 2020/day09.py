data = [int(x) for x in open('inputs/input09.txt').read().strip().split('\n')]


def sum_of_2(pos, num, prev=25):
    lbound = pos - prev
    num_range = data[lbound:pos]
    return any(num - n in num_range for n in num_range if n != num - n)


prev_range = 25
for pos, num in enumerate(data[prev_range:]):
    if not sum_of_2(pos + prev_range, num, prev_range):
        print(f'Part 1: {num}')
        invalid = num
        break

for pos in range(len(data)):
    weakness = []
    while sum(weakness) <= invalid:
        if sum(weakness) == invalid:
            print(f'Part 2: {min(weakness) + max(weakness)}')
            break
        weakness.append(data[pos])
        pos += 1
    else:
        continue
    break
