from hashlib import md5


def hash_starts_with(n):
    num = 0
    while True:
        if md5((inp + str(num)).encode()).hexdigest().startswith(n):
            return num
        num += 1


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        inp = f.read().strip()

    print(hash_starts_with("00000"))
