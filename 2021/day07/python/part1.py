def count_fuel(pos):
    return sum(abs(num - pos) for num in positions)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        positions = [int(num) for num in f.read().split(',')]

    fuel_cost = {count_fuel(i) for i in range(min(positions), max(positions) + 1)}

    print(min(fuel_cost))
