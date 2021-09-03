

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


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        num = int(f.read())

    for _ in range(40):
        num = look_and_say(str(num))

    print(len(num))

