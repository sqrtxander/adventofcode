import functools


@functools.lru_cache
def get_value(key):
    try:
        return int(key)
    except ValueError:
        pass

    cmd = instructions[key].split(' ')

    if 'AND' in cmd:
        return get_value(cmd[0]) & get_value(cmd[2])
    elif 'NOT' in cmd:
        return ~get_value(cmd[1]) & int('1111111111111111', 2)
    elif 'OR' in cmd:
        return get_value(cmd[0]) | get_value(cmd[2])
    elif 'RSHIFT' in cmd:
        return get_value(cmd[0]) >> get_value(cmd[2])
    elif 'LSHIFT' in cmd:
        return get_value(cmd[0]) << get_value(cmd[2])
    else:
        return get_value(cmd[0])


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        instructions = {z.split(' -> ')[1].strip(): z.split(' -> ')[0] for z in f.readlines()}

    instructions['b'] = str(get_value('a'))
    get_value.cache_clear()
    print(get_value('a'))
