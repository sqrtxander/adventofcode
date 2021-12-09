if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [[x.split() for x in line.split(' | ')] for line in f.read().splitlines()]

    count = 0

    for (entries, output) in data:
        entries = sorted(entries, key=len)
        zero = set()
        one = set(entries[0])
        two = set()
        three = set()
        four = set(entries[2])
        five = set()
        six = set()
        seven = set(entries[1])
        eight = set(entries[9])
        nine = set()

        for entry in entries[3:9]:
            entry = set(entry)
            if len(entry) == 6:
                if len(entry.intersection(four)) == 4:
                    nine = entry
                elif len(entry.intersection(seven)) == 2:
                    six = entry
                else:
                    zero = entry
            elif len(entry) == 5:
                if len(entry.intersection(one)) == 2:
                    three = entry
                elif len(entry.intersection(four)) == 3:
                    five = entry
                else:
                    two = entry

        current = ''
        for entry in output:
            entry = set(entry)
            if entry == zero:
                current += '0'
            elif entry == one:
                current += '1'
            elif entry == two:
                current += '2'
            elif entry == three:
                current += '3'
            elif entry == four:
                current += '4'
            elif entry == five:
                current += '5'
            elif entry == six:
                current += '6'
            elif entry == seven:
                current += '7'
            elif entry == eight:
                current += '8'
            elif entry == nine:
                current += '9'

        count += int(current)

    print(count)
