import re
import json

test = [1, {1: "b", "blue": [1, 2]}, ["red", {'b': "red", 'a': 5}]]


def sum_nums(inp):
    nums = [int(x) for x in re.findall(r'-?\d+', str(inp))]
    return sum(nums)


def sum_red(inp):
    if type(inp) == int:
        return 0
    if type(inp) == list:
        return sum(sum_red(x) for x in inp)
    if type(inp) == str:
        return 0
    if type(inp) == dict:
        if 'red' in inp.values():
            return sum_nums(inp)
        return sum_red(list(inp.values()))


with open('inputs/input12.json', 'r') as f:
    data = json.loads(f.read())

total_sum = sum_nums(data)
red_sum = sum_red(data)
print(total_sum)
print(total_sum-red_sum)
