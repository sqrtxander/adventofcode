import re

test = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''

# open('inputs/input07.txt').read()
data = {}
for line in test.strip().split('\n'):
    command, key = line.split(' -> ')
    data[key.strip()] = command


def get_value(key):
    try:
        return int(key)
    except ValueError:
        pass

    cmd = data[key].split(' ')

    if 'AND' in cmd:
        return get_value(cmd[0]) & get_value(cmd[2])
    elif 'NOT' in cmd:
        return ~get_value(cmd[1])
    elif 'OR' in cmd:
        return get_value(cmd[0]) | get_value(cmd[2])
    elif 'RSHIFT' in cmd:
        return get_value(cmd[0]) >> get_value(cmd[2])
    elif 'LSHIFT' in cmd:
        return get_value(cmd[0]) << get_value(cmd[2])
    else:
        return get_value(cmd[0])


print(get_value('h'))
print(~ 5)
