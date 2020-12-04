data = open('inputs/input08.txt').read().strip().split('\n')

sum_str_len = sum(len(x) for x in data)
sum_str_memory = sum(len(eval(x)) for x in data)
sum_str_encode = sum(len(repr(x).replace('"', '\\"')) for x in data)

print(f'Part 1: {sum_str_len - sum_str_memory}')
print(f'Part 2: {sum_str_encode - sum_str_len}')
