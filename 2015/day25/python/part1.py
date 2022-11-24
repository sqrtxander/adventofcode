def solve(file):
    def get_cell_no(r, c):
        return (r + c - 2) * (r + c - 1) // 2 + c
    
    with open(file, 'r') as f:
        row, col = [int(line) for line in f.read().split(',')]
        
    code = 20151125

    cell = get_cell_no(row, col)

    for _ in range(1, cell):
        code = (code * 252533) % 33554393
    return code

if __name__ == '__main__':
    
    print(solve('../input.in'))
