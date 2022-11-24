from functools import reduce
import itertools


def solve(file):
    with open(file, 'r') as f:
        weights = set(int(line) for line in f.read().splitlines())
    
    individual_weight = sum(weights) // 4   
    done = False
    smallest = float('inf')

    for i in range(1, len(weights)):
        for combo in itertools.combinations(weights, i):
            if sum(combo) == individual_weight:
                res = reduce(lambda x, y: x * y, combo)
                if res < smallest:
                    smallest = res
                done = True
        if done:
            break
    return smallest

if __name__ == '__main__':

    EXPECTED = 44
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
