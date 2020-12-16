data = [line.strip().split(' = ') for line in open('inputs/input14.txt').readlines()]
mem = {}
mask = None
for cmd, inp in data:
    if cmd == 'mask':
        mask = inp
    else:
        pos = cmd[4:-1]
        inp = list(bin(int(inp))[2:].zfill(36))
        for i, num in enumerate(mask):
            if num != 'X':
                inp[i] = num

        inp = ''.join(inp)
        mem[pos] = int(inp, 2)

print(f'Part 1: {sum(mem.values())}')

mem = {}
x_pos = None
mask = None
for cmd, inp in data:
    if cmd == 'mask':
        mask = inp
        x_pos = [i for i, x in enumerate(mask) if x == 'X']
    else:
        pos = list(bin(int(cmd[4:-1]))[2:].zfill(36))
        for i, num in enumerate(mask):
            if num != '0':
                pos[i] = num
        for x in range(0, 2**len(x_pos)):
            sto_pos = pos
            x = bin(x)[2:].zfill(len(x_pos))
            for i, c in enumerate(x):
                sto_pos[x_pos[i]] = c

            sto_pos = int(''.join(sto_pos), 2)
            mem[sto_pos] = int(inp)


print(f'Part 2: {sum(mem.values())}')
