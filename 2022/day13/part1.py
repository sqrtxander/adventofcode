import os
import json


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 13
TEST_INPUT = '''\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = compare(l, r)
            if result is not None:
                return result
        if len(left) == len(right):
            return None
        else:
            return len(left) < len(right)

    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)


def solve(inp):
    total = 0
    pairs = inp.strip().split('\n\n')
    for i, pair in enumerate(pairs, start=1):
        l1, l2 = pair.splitlines()
        if compare(json.loads(l1), json.loads(l2)):
            total += i

    return total


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
