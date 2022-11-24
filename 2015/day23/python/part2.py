def solve(file):
    with open(file, 'r') as f:
        data = [line.split() for line in f.read().splitlines()]
    
    registers = {'a': 1, 'b': 0}
    i = 0

    while i < len(data):
        instruction = data[i]
    
        if instruction[0] == 'hlf':
            registers[instruction[1]] //= 2
        elif instruction[0] == 'tpl':
            registers[instruction[1]] *= 3
        elif instruction[0] == 'inc':
            registers[instruction[1]] += 1
        elif instruction[0] == 'jmp':
            i += int(instruction[1])
            continue
        elif instruction[0] == 'jie':
            if registers[instruction[1][:-1]] % 2 == 0:
                i += int(instruction[2])
                continue
        elif instruction[0] == 'jio':
            if registers[instruction[1][:-1]] == 1:
                i += int(instruction[2])
                continue
        i += 1

    return registers['b'] 
            

if __name__ == '__main__':

    EXPECTED = 0
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
