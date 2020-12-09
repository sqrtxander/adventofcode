data = [[i, int(j)] for i, j in [x.split(' ') for x in open('inputs/input08.txt').readlines()]]


def solve():
    acc = pos = 0
    v = [False] * len(data)
    while pos < len(data):
        if v[pos]:
            return acc, False
        v[pos] = True
        inst, arg = data[pos]
        if inst == 'acc':
            acc += arg
        elif inst == 'jmp':
            pos += arg
            continue

        pos += 1

    return acc, True


print(f'Part 1: {solve()[0]}')


for pos in range(len(data)):
    if data[pos][0] != 'acc':
        data[pos][0] = 'jmp' if data[pos][0] == 'nop' else 'nop'  # switch instruction
        ans = solve()
        data[pos][0] = 'jmp' if data[pos][0] == 'nop' else 'nop'  # switch back
    else:
        continue

    if ans[1]:
        print(f'Part 2: {ans[0]}')
        break
