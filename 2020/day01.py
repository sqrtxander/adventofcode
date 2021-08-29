import time

with open('inputs/input01.txt', 'r') as f:
    nums = set(int(x) for x in f.readlines())

t = time.perf_counter()

for i in nums:
    if 2020 - i in nums:
        print(f'Part 1: {i * (2020 - i)}')
        break

for i in nums:
    for j in nums:
        if 2020 - i - j in nums:
            print(f'Part 2: {i * (2020 - i - j) * j}')
            break
    else:
        continue
    break

print(time.perf_counter() - t)