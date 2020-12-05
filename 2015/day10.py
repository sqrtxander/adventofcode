num = 1113122113


def look_and_say(n):
    shortened = ''
    my_iter = iter(str(n))
    current = next(my_iter)
    count = 1
    for s in my_iter:
        if s != current:
            shortened += f'{count}{current}'
            current = s
            count = 1
        else:
            count += 1
    shortened += f'{count}{current}'
    return shortened


for _ in range(40):
    num = look_and_say(str(num))

print(f'Part 1: {len(num)}')

for _ in range(10):
    num = look_and_say(num)

print(f'Part 2: {len(num)}')
