from copy import deepcopy

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = f.read().splitlines()

    o2 = deepcopy(data)
    co2 = deepcopy(data)

    for i in range(len(o2[0])):
        bits = [num[i] for num in o2]

        if len(o2) > 1:
            if bits.count('1') >= bits.count('0'):
                o2 = [n for n in o2 if n[i] == '1']
            else:
                o2 = [n for n in o2 if n[i] == '0']

    for i in range(len(co2[0])):
        bits = [num[i] for num in co2]

        if len(co2) > 1:
            if bits.count('1') >= bits.count('0'):
                co2 = [n for n in co2 if n[i] == '0']
            else:
                co2 = [n for n in co2 if n[i] == '1']

    o2 = int(o2[0], 2)
    co2 = int(co2[0], 2)

    print(o2*co2)

