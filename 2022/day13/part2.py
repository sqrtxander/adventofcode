import os
import json


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 140
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


def sort(packets):
    for i in range(len(packets)):
        for j in range(i + 1, len(packets)):
            if not compare(packets[i], packets[j]):
                packets[i], packets[j] = packets[j], packets[i]
    return packets


def solve(inp):
    total = 0
    packets = [json.loads(packet)
               for packet in inp.strip().replace('\n\n', '\n').split('\n')]
    packets.extend([[[2]], [[6]]])
    packets = sort(packets)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
