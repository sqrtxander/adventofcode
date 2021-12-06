from collections import Counter

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        ages = Counter([int(num) for num in f.read().split(',')])

    for _ in range(256):
        ages = {n: ages[n + 1] for n in range(-1, 8)}
        ages[8] = ages[-1]
        ages[6] += ages[-1]
        ages[-1] = 0

    print(sum(ages.values()))
