from copy import deepcopy

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = f.read().splitlines()

    o2_list = deepcopy(data)
    co2_list = deepcopy(data)

    while len(o2_list) > 1:
        for x in range(len(o2_list[0])):
            one_count = 0
            zero_count = 0
            for i in o2_list:
                if i[x] == '1':
                    one_count += 1
                if i[x] == '0':
                    zero_count += 1

            if len(o2_list) > 1:
                if one_count >= zero_count:
                    o2_list = [n for n in o2_list if n[x] == '1']
                else:
                    o2_list = [n for n in o2_list if n[x] == '0']

    while len(co2_list) > 1:
        for x in range(len(co2_list[0])):
            one_count = 0
            zero_count = 0
            for i in co2_list:
                if i[x] == '1':
                    one_count += 1
                if i[x] == '0':
                    zero_count += 1

            if len(co2_list) > 1:
                if one_count >= zero_count:
                    co2_list = [n for n in co2_list if n[x] == '0']
                else:
                    co2_list = [n for n in co2_list if n[x] == '1']

    o2 = int(o2_list[0], 2)
    co2 = int(co2_list[0], 2)

    print(o2*co2)

