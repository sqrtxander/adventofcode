def solve(file):
    def break_into_n_sides(n, sides):
        for i in range(0, len(sides), n):
            yield sides[i:i + n]

    with open(file, 'r') as f:
        all_sides = [[int(num) for num in line.split()] for line in f.read().splitlines()]
    
    all_sides = sum(([*break_into_n_sides(3, sides)] for sides in  zip(*all_sides)), [])

    return sum([max(sides) < sum(sides) - max(sides) for sides in all_sides])

    
if __name__ == '__main__':

    print(solve('../input.in'))
