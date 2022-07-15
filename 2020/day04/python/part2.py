import re

def solve(file):
    with open(file, 'r') as f:
        data = [{(es := e.split(":"))[0]: es[1]for e in
                p.replace("\n", " ").strip().split(" ")}
                for p in f.read().strip().split("\n\n")]

    valid = [passport for passport in data if all(field in passport
             for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))]   
    valid = [passport for passport in valid if 1920 <= int(passport['byr']) <= 2002]
    valid = [passport for passport in valid if 2010 <= int(passport['iyr']) <= 2020]
    valid = [passport for passport in valid if 2020 <= int(passport['eyr']) <= 2030]
    valid = [passport for passport in valid if passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193
             or passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76]
    valid = [passport for passport in valid if re.fullmatch(r'#[0-9a-f]{6}', passport['hcl'])]
    valid = [passport for passport in valid if passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')]
    valid = [passport for passport in valid if re.fullmatch(r'[0-9]{9}', passport['pid'])]

    return len(valid)

if __name__ == '__main__':

    EXPECTED = 0
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
