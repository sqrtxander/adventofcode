num = 29000000


house = 0
presents = 0
while presents < num:
    house += 1
    presents = 0
    for i in range(1, int(house ** 0.5) + 1):
        if house % i == 0:
            presents += (i + house//i) * 10
print(house)


house = 0
presents = 0
while presents < num:
    house += 1
    presents = 0
    for i in range(1, int(house ** 0.5) + 1):
        if house % i == 0:
            if house//i <= 50:
                presents += i * 11
            if i <= 50:
                presents += house//i * 11

print(house)

