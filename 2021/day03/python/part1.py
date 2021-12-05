if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = f.read().splitlines()

    gamma = [''] * len(data[0])
    epsilon = [''] * len(data[0])

    for i in range(len(data[0])):
        bits = [num[i] for num in data]

        if bits.count('1') >= bits.count('0'):
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    print(gamma * epsilon)
