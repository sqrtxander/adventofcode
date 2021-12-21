from collections import defaultdict


def get_neighbours(x, y):
    yield x-1, y-1
    yield x, y-1
    yield x+1, y-1
    yield x-1, y
    yield x, y
    yield x+1, y
    yield x-1, y+1
    yield x, y+1
    yield x+1, y+1


def enhance(enhancement, image):
    min_x = min(x for x, _ in image)
    max_x = max(x for x, _ in image)
    min_y = min(y for _, y in image)
    max_y = max(y for _, y in image)

    default_num = str(image.default_factory()) * 9
    char = enhancement[int(default_num, 2)]
    if char == '#':
        new_image = defaultdict(lambda: 1)
    elif char == '.':
        new_image = defaultdict(lambda: 0)
    else:
        raise AssertionError

    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            num_str = ''
            for nx, ny in get_neighbours(x, y):
                num_str += str(image[(nx, ny)])
            char = enhancement[int(num_str, 2)]
            if char == '#':
                new_image[(x, y)] = 1
            elif char == '.':
                new_image[(x, y)] = 0
            else:
                raise AssertionError

    return new_image



def parse(file):
    with open(file, 'r') as f:
        enhancement, data = f.read().split('\n\n')

        image = defaultdict(int)
        for y, line in enumerate(data.split('\n')):
            for x, pos in enumerate(line):
                if pos == '#':
                    image[(x, y)] = 1
                elif pos == '.':
                    image[(x, y)] = 0
                else:
                    raise AssertionError

        return enhancement, image


def solve(enhancement, image):
    for _ in range(2):
        image = enhance(enhancement, image)

    return list(image.values()).count(1)


if __name__ == '__main__':
    EXPECTED = 35
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))
