import os


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
EXPECTED = 95437
TEST_INPUT = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''


def solve(inp):
    def get_size(dir_):
        return sum(size for file_, size in files.items() if file_.startswith(dir_))

    data = [line for line in inp.strip().splitlines()]

    current_dir = '/'
    dirs = ['/']
    files = {}

    for line in data:
        if line == '$ cd ..':
            current_dir = os.path.dirname(current_dir)
        elif line.startswith('$ cd'):
            current_dir = os.path.join(current_dir, line.split(' ')[-1])
        elif line.startswith('dir '):
            dirs.append(os.path.join(current_dir, line.split(' ')[-1]))
        elif line[0].isdecimal():
            size, file_ = line.split(' ')
            files[os.path.join(current_dir, file_)] = int(size)
        elif line == '$ ls':
            continue
        else:
            raise AssertionError(line)

    total = 0
    for dir_ in dirs:
        size = get_size(dir_)
        if size <= 100000:
            total += size
    return total


def main():
    test = solve(TEST_INPUT)
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'

    with open(INPUT_TXT, 'r') as f:
        print(solve(f.read()))


if __name__ == '__main__':
    main()
