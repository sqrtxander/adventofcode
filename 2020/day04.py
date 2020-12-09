import re

data = [{(es := e.split(":"))[0]: es[1]for e in p.replace("\n", " ").strip().split(" ")}for p in open('inputs/input04.txt').read().strip().split("\n\n")]

valid_1, valid_2 = 0, 0
for passport in data:
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
        valid_1 += 1
    else:
        continue
    if not 1920 <= int(passport['byr']) <= 2002:
        continue
    if not 2010 <= int(passport['iyr']) <= 2020:
        continue
    if not 2020 <= int(passport['eyr']) <= 2030:
        continue
    if passport['hgt'].endswith('cm'):
        if not 150 <= int(passport['hgt'][:-2]) <= 193:
            continue
    elif passport['hgt'].endswith('in'):
        if not 59 <= int(passport['hgt'][:-2]) <= 76:
            continue
    else:
        continue
    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
        continue
    if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        continue
    if not re.fullmatch(r'[0-9]{9}', passport['pid']):
        continue

    valid_2 += 1

print(f'Part 1: {valid_1}')
print(f'Part 2: {valid_2}')
