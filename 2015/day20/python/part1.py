if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        num = int(f.read())

    house = 0
    presents = 0
    while presents < num:
        house += 1
        presents = 0
        for i in range(1, int(house ** 0.5) + 1):
            if house % i == 0:
                presents += (i + house//i) * 10
    print(house)
