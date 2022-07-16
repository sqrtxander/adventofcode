def solve(file):
    with open(file, 'r') as f:
        homework = f.read().splitlines()
    
    



if __name__ == '__main__':

    EXPECTED = 13632
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
