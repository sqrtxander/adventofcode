data = [int(x) for x in open('inputs/input02.txt').read().split(',')]


def comp_intcode(data, noun, verb):
    data[1] = noun
    data[2] = verb
    op_pos = 0
    while True:
        opcode = data[op_pos]
        output_pos = data[op_pos + 3]
        num_1 = data[data[op_pos + 1]]
        num_2 = data[data[op_pos + 2]]

        if opcode == 1:
            data[output_pos] = num_1 + num_2
        elif opcode == 2:
            data[output_pos] = num_1 * num_2
        elif opcode == 99:
            break
        else:
            pass

        op_pos += 4
    return data[0]


def comp_part_2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            copy_data = data.copy()
            if comp_intcode(copy_data, noun, verb) == 19690720:
                return 100 * noun + verb


print(f'day 1: {comp_intcode(data.copy(), 12, 2)}')
print(f'day 2: {comp_part_2()}')
