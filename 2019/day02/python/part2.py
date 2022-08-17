def run_intcode(program, noun=None, verb=None):
    if noun is not None:
        program[1] = noun
    if verb is not None:
        program[2] = verb

    for i in range(0, len(program), 4):
        opcode, read1, read2, store = program[i: i+4]

        if opcode == 1:
            program[store] = program[read1] + program[read2]
        elif opcode == 2:
            program[store] = program[read1] * program[read2]
        elif opcode == 99:
            break

    return program[0]


def solve(file):
    with open(file, 'r') as f:
        program = [int(num) for num in f.read().split(',')]
    
    for noun in range(100):
        for verb in range(100):
            if run_intcode(program.copy(), noun, verb) == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':

    print(solve('../input.in'))

