data = open('inputs/input03.txt').read().strip().split('\n')


def count_trees(right, down):
    x, y = 0, 0
    tree_count = 0
    while y < len(data):
        if data[y][x] == '#':
            tree_count += 1
        x += right
        x %= len(data[y])
        y += down
    return tree_count


total_trees = 1

for right_count, down_count in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    total_trees *= count_trees(right_count, down_count)

print(f'Part 1: {count_trees(3, 1)}')
print(f'Part 2: {total_trees}')
