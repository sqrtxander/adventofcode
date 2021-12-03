if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = f.read().splitlines()

    gamma = list(data[0])
    epsilon = list(data[0])

    for x in range(len(data[0])):
        one_count = 0
        zero_count = 0
        for i in data:
            if i[x] == '1':
                one_count += 1
            if i[x] == '0':
                zero_count += 1

        if one_count > zero_count:
            gamma[x] = '1'
            epsilon[x] = '0'
        else:
            gamma[x] = '0'
            epsilon[x] = '1'

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    print(gamma * epsilon)
