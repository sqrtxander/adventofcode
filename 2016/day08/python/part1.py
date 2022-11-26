def solve(file):
    with open(file, 'r') as f:
        sequence = [line.split() for line in f.read().splitlines()]

    width, height = 50, 6
    screen = {(x, y): 0 for x in range(width) for y in range(height)}

    for instruction in sequence:
        if instruction[0] == 'rect':
            x, y = (int(n) for n in instruction[1].split('x'))
            for i in range(x):
                for ii in range(y):
                    screen[(i, ii)] = 1

        elif instruction[1] == 'row':
            row, shift = int(instruction[2].split('=')[1]), int(instruction[4])
            store = [screen[(x, row)] for x in range(width)]
            for i in range(width):
                screen[(i, row)] = store[(i - shift) % width]
            

        elif instruction[1] == 'column':
            column, shift = int(instruction[2].split('=')[1]), int(instruction[4])
            store = [screen[(column, y)] for y in range(height)]
            for i in range(height):
                screen[(column, i)] = store[(i - shift) % height]
          
    return sum(screen.values())
    
if __name__ == '__main__':

    EXPECTED = 6
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
