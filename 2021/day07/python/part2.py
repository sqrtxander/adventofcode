def sum_fuel(pos):
    return sum(abs(num-pos)*(abs(num-pos)+1)//2 for num in crabs)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        crabs = [int(num) for num in f.read().split(',')]

    fuel_cost = {sum_fuel(i) for i in range(min(crabs), max(crabs) + 1)}

    print(min(fuel_cost))
