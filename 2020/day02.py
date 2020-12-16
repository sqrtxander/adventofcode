import re

data = [(int(a), int(b), c, d) for a, b, c, d in re.findall(r'(\d+)-(\d+) (\w): (\w+)', open('inputs/input02.txt').read())]

correct_pass_1, correct_pass_2 = 0, 0
for rulel, ruleu, key, password in data:
    
    if rulel <= password.count(key) <= ruleu:
        correct_pass_1 += 1

    if (password[rulel-1] == key) ^ (password[ruleu-1] == key):
        correct_pass_2 += 1

print(f'Part 1: {correct_pass_1}')
print(f'Part 2: {correct_pass_2}')

