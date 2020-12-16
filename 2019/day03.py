data = [x.split(',') for x in [line for line in open('inputs/input03.txt').readlines()]]


def increment_xy(wire):
    wire_plot = []
    x, y = [0, 0]
    for i in wire:
        for j in range(int(i[1:])):
            wire_plot.append((x, y))
            if i[0] == 'R':
                x += 1
            elif i[0] == 'L':
                x -= 1
            elif i[0] == 'U':
                y += 1
            elif i[0] == 'D':
                y -= 1
            else:
                print('Data error.')
                break
    return wire_plot


def navigate():
    wire_1 = increment_xy(data[0])
    wire_2 = increment_xy(data[1])
    intercepts = list(set(wire_1) & (set(wire_2)))
    abs_intercepts = [(abs(i[0]), abs(i[1])) for i in intercepts]
    return min(sum(i) for i in abs_intercepts if sum(i) > 0)


def combined_length():
    wire_1 = increment_xy(data[0])
    wire_2 = increment_xy(data[1])
    intercepts = list(set(wire_1) & (set(wire_2)))
    total_len_list = []
    for i in intercepts:
        wire_1_len = len(wire_1[:wire_1.index(i)])
        wire_2_len = len(wire_2[:wire_2.index(i)])
        total_len_list.append(wire_1_len + wire_2_len)
    total_len_list.remove(0)
    return min(total_len_list)


print(f'Part 1: {navigate()}')
print(f'Part 2: {combined_length()}')
