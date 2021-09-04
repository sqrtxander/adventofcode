import re


def get_total(amounts):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for i in range(len(ingredients)):
        capacity += stats[ingredients[i]][0] * amounts[i]
        durability += stats[ingredients[i]][1] * amounts[i]
        flavor += stats[ingredients[i]][2] * amounts[i]
        texture += stats[ingredients[i]][3] * amounts[i]
    if any(stat < 0 for stat in (capacity, durability, flavor, texture)):
        return 0
    return capacity * durability * flavor * texture


if __name__ == '__main__':
    ingredients = []
    stats = {}
    with open('../input.txt', 'r') as f:
        for line in f:
            i, cp, d, f, t, cl = re.findall(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)[0]
            ingredients.append(i)
            stats[i] = (int(cp), int(d), int(f), int(t), int(cl))

    valid = set()
    for su in range(100 + 1):
        for sp in range(100 + 1 - su):
            for ca in range(100 + 1 - su - sp):
                ch = 100 - su - sp - ca
                valid.add(get_total((su, sp, ca, ch)))

    print(max(valid))
