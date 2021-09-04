import re
import json


def sum_nums(inp):
    nums = [int(x) for x in re.findall(r'-?\d+', str(inp))]
    return sum(nums)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = json.loads(f.read())

    total_sum = sum_nums(data)
    print(total_sum)
