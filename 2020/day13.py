from math import ceil
from sympy.ntheory.modular import crt
import operator as op

test = '''939
7,13,x,x,59,x,31,19'''
# open('inputs/input13.txt').readlines()
data = [x.strip() for x in open('inputs/input13.txt').readlines()]

time = int(data[0])
offsets, buses = zip(*[(t, int(x)) for t, x in enumerate(data[1].split(',')) if x != 'x'])
# bus_ids = ((17, 0), (13, 2), (19, 3))
print(time, buses)

best = None
for bus in buses:
    score = ceil(time / bus) * bus - time
    if best is None or score < best[0]:
        best = (score, bus)
print(f'Part 1: {best[0] * best[1]}')

print(f'Part 2: {crt(buses, map(op.neg, offsets))[0]}')
