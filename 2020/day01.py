data = [int(x) for x in open('inputs/input01.txt').readlines()]

for i in data:
    if 2020 - i in data:
        print(f'Part 1: {i * (2020 - i)}')
        break

for i in data:
    for j in data[data.index(i) + 1:]:
        if 2020 - i - j in data:
            print(f'Part 2: {i * (2020 - i - j) * j}')
            break
    else:
        continue
    break
