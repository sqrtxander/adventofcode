def solve(file):
    with open(file, 'r') as f:
        data = [{(es := e.split(":"))[0]: es[1]for e in
                p.replace("\n", " ").strip().split(" ")}
                for p in f.read().strip().split("\n\n")]

    return sum(all(field in passport for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')) for passport in data)


if __name__ == '__main__':

    EXPECTED = 2
    test = solve('../test.in')
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve('../input.in'))
