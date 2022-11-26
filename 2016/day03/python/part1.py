def solve(file):
    with open(file, 'r') as f:
        all_sides = [[int(num) for num in line.split()] for line in f.read().splitlines()]
    
    return sum([max(sides) < sum(sides) - max(sides) for sides in all_sides])


if __name__ == '__main__':

    print(solve('../input.in'))
