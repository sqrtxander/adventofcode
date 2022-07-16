def solve(file):
    with open(file, 'r') as f:
        orbits = {b: a for a, b in (line.split(')') for line in f.read().splitlines())}

    count = 0
    for planet in orbits:
        while planet in orbits:
            planet = orbits[planet]
            count += 1
    return count

    
if __name__ == '__main__':

    EXPECTED = 42
    test = solve('../test1.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
