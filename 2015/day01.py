import time

data = open('inputs/input01.txt').read()

t = time.perf_counter()

print(f'Part 1: {data.count("(") - data.count(")")}')

for char in range(len(data)):
    # if entered basement
    if data[:char].count("(") < data[:char].count(")"):
        print(f'Part 2: {char}')
        break

print(f'Time elapsed: {time.perf_counter() - t} seconds')
