data = [int(line) for line in open('inputs/input01.txt').readlines()]

ans = 0
for i in data:
    ans += i // 3 - 2
print(f'part 1: {ans}')

ans = 0
for i in data:
    while True:
        i = i // 3 - 2
        if i <= 0:
            break
        ans += i
print(f'part 2: {ans}')



