from hashlib import md5

data = 'bgvyzdsv'


def hash_starts(starts_with):
    num = 0
    while True:
        if md5((data + str(num)).encode()).hexdigest().startswith(starts_with):
            return num
        num += 1


print(f'Part 1: {hash_starts("00000")}')
print(f'Part 2: {hash_starts("000000")}')
