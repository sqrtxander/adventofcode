data = {(b := ln.replace(" bags", "").replace(" bag", "").split(" contain "))[0]: {c[2::]: int(c[0]) for c in b[1].strip().replace(".", "").split(", ") if c != "no other"} for ln in open("inputs/input07.txt").readlines()}


def count_outer_bags(colour='shiny gold'):

    def bag1_contains_bag2(bag1, looking_for):
        if looking_for in data[bag1]:
            return True

        for bag in data[bag1]:
            if bag1_contains_bag2(bag, looking_for):
                return True
            else:
                continue

    bags_hold_count = 0
    for parent in data:

        if colour in data[parent]:
            bags_hold_count += 1
        else:
            for bag_count in data[parent]:
                if bag1_contains_bag2(bag_count, colour):
                    bags_hold_count += 1
                    break
    return bags_hold_count


def count_inner_bags(parent='shiny gold'):
    return sum(number + number * count_inner_bags(c) for c, number in data[parent].items())


print(f'Part 1: {count_outer_bags()}')
print(f'Part 2: {count_inner_bags()}')
