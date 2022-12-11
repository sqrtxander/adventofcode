import os
from functools import partial


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 10605
TEST_INPUT = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''


def solve(inp):
    def power(a, b):
        return a ** b

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    monkeys = []
    for chunk in inp.strip().split('\n\n'):
        lines = chunk.splitlines()
        monkey = {}
        monkey['items'] = [int(x) for x in lines[1].split(':')[
            1].strip().split(',')]
        if 'old * old' in lines[2]:
            val = 'old * old'
            monkey['operation'] = partial(power, b=2)
        elif '+' in lines[2]:
            val = int(lines[2].split('+')[1].strip())
            monkey['operation'] = partial(add, val)
        elif '*' in lines[2]:
            val = int(lines[2].split('*')[1].strip())
            monkey['operation'] = partial(multiply, val)

        monkey['test'] = (int(lines[3].split(' ')[-1].strip()), int(
            lines[4].split(' ')[-1].strip()), int(lines[5].split(' ')[-1].strip()))
        monkey['inspected'] = 0
        monkeys.append(monkey)

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey['items']:
                item = monkey['operation'](item) // 3

                test, true, false = monkey['test']
                if item % test == 0:
                    monkeys[true]['items'].append(item)
                else:
                    monkeys[false]['items'].append(item)
                monkey['inspected'] += 1
            monkey['items'].clear()

    inspected = sorted([monkey['inspected'] for monkey in monkeys])
    return inspected[-1] * inspected[-2]


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
