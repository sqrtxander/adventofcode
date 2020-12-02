data = [x.split(' ') for x in open('inputs/input02.txt').read().strip().split('\n')]
for x in range(len(data)):
    data[x][0] = [int(x) for x in data[x][0].split('-')]
    data[x][1] = data[x][1][0]

correct_pass_1, correct_pass_2 = 0, 0
for rule, key, password in data:
    
    if rule[0] <= password.count(key) <= rule[1]:
        correct_pass_1 += 1

    if (password[rule[0]-1] == key) ^ (password[rule[1]-1] == key):
        correct_pass_2 += 1

print(f'Part 1: {correct_pass_1}')
print(f'Part 2: {correct_pass_2}')

