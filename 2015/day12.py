import re
import json


def sum_nums(inp):
    nums = [int(x) for x in re.findall(r'-?\d+', inp)]
    return sum(nums)


def check_red(inp):
    for el in inp:
        if type(el) == dict:
            if 'red' in el.values() or 'red' in el.keys():
                yield sum_nums(str(el))
            else:
                yield check_red(el)
        else:
            yield check_red(el)


with open('inputs/input12.json', 'r') as f:
    data = json.load(f)


total_sum = sum_nums(str(data))
print(total_sum)


s = 0
for num in list(check_red(data)):
    s += num
    print(num)

print(total_sum - s)


# 142353 too high
# 75454 too low
# not 129421