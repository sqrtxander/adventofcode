def parse(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


def solve(hex_str):

    def read(bin_str):
        total = 0
        while len(bin_str) > 0:
            version = int(bin_str[:3], 2)
            total += version
            typeid = int(bin_str[3:6], 2)
            bin_str = bin_str[6:]
            i = 0

            if typeid == 4:
                packet = ''
                while bin_str[i] == '1':
                    packet += bin_str[i + 1:i + 5]
                    i += 5
                packet += bin_str[i + 1:i + 5]
                bin_str = bin_str[i + 5:]
                return int(packet, 2)

                bin_str = bin_str.lstrip('0')


            lentypeid = int(bin_str[0], 2)
            bin_str = bin_str[1:]
            if lentypeid == 0:
                lenpackets = int(bin_str[:15], 2)
                bin_str = bin_str[15:]
                total += read(bin_str[:lenpackets])
            # else:
            #     numpackets = int(bin_str[:11], 2)

            bin_str = bin_str.lstrip('0')
        return total

    bin_str = bin(int(hex_str, 16))[2:]
    bin_str = bin_str.zfill(len(bin_str) + len(bin_str) % 4)
    print(read(bin_str))


if __name__ == '__main__':
    EXPECTED = 16
    test = solve(parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(parse('../input.in')))
