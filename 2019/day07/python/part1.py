from itertools import permutations


def run_intcode(program, inps, noun=None, verb=None):
    if noun is not None:
        program[1] = noun
    if verb is not None:
        program[2] = verb

    inp_count = 0
    i = 0
    while True:
        opcode = program[i]
        opc_str = str(opcode).zfill(5)
        opcode = int(opc_str[-2:])
        mode1 = int(opc_str[2])
        mode2 = int(opc_str[1])
        mode3 = int(opc_str[0])

        if opcode == 1:
            read1, read2, store = program[i+1: i+4]
            if mode1 == 0:
                read1 = program[read1]
            if mode2 == 0:
                read2 = program[read2]

            program[store] = read1 + read2

            i += 4
        elif opcode == 2:
            read1, read2, store = program[i+1: i+4]
            if mode1 == 0:
                read1 = program[read1]
            if mode2 == 0:
                read2 = program[read2]
            
            program[store] = read1 * read2          
            
            i += 4
        elif opcode == 3:
            store = program[i+1]
            program[store] = inps[inp_count]
            inp_count += 1
        
            i += 2
        elif opcode == 4:
            read1 = program[i+1]
            print(f'output: {program[read1]}')
        
            i += 2
        elif opcode == 5:
            read1, read2 = program[i+1: i+3]
            if mode1 == 0:
                read1 = program[read1]
            if mode2 == 0:
                read2 = program[read2]
            if read1 != 0:
                i = read2
            else:
                i += 3
        elif opcode == 6:
            read1, read2 = program[i+1: i+3]
            if mode1 == 0:
                read1 = program[read1]
            if mode2 == 0:
                read2 = program[read2]
            if read1 == 0:
                i = read2
            else:
                i += 3
        elif opcode == 7:
            read1, read2, store = program[i+1: i+4]
            if mode1 == 0:
                read1 = program[read1]
            if mode2 == 0:
                read2 = program[read2]
            if read1 < read2:
                program[store] = 1
            else:
                program[store] = 0
            i += 4
        elif opcode == 8:
            read1, read2, store = program[i+1: i+4]
            if mode1 == 0:
                read1 = program[read1]
            if mode2 == 0:
                read2 = program[read2]
            if read1 == read2:
                program[store] = 1
            else:
                program[store] = 0
            i += 4
        
        elif opcode == 99:
            break
        else:
            raise ValueError(f'Unknown opcode {opcode}')


def solve(file):
    with open(file, 'r') as f:
        data = [int(num) for num in f.read().split(',')]

    for A, B, C, D, E in permutations(range(5)):

    # return run_intcode(data, [1])    

if __name__ == '__main__':

    print(solve('../input.in'))
