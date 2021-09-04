import itertools
import math


class Character:
    def __init__(self, hp, dam, arm):
        self.health_init = hp
        self.damage = dam
        self.armor = arm
        self.health = self.health_init

    def damage_per_hit(self, opponent):
        hit = self.damage - opponent.armor
        hit = hit if hit >= 1 else 1
        return hit

    def reset(self):
        self.health = self.health_init


def p1_wins_fight(p1, p2):
    p1_hit = p1.damage_per_hit(p2)
    p2_hit = p2.damage_per_hit(p1)
    return math.ceil(p2.health/p1_hit) <= math.ceil(p1.health/p2_hit)


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        boss_hp, boss_dam, boss_arm = [int(x.split(': ')[-1]) for x in f.readlines()]

    weapons = ((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0))
    armor = ((13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0))
    rings = ((25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3))

    boss = Character(boss_hp, boss_dam, boss_arm)

    losing_costs = set()
    for wc, wd, wa in weapons:
        for ac, ad, aa in armor:
            for i in range(3):
                for j in itertools.combinations(rings, i):
                    cost = wc + ac + sum(c[0] for c in j)
                    damage = wd + ad + sum(d[1] for d in j)
                    defence = wa + aa + sum(a[2] for a in j)

                    player = Character(100, damage, defence)
                    boss.reset()
                    if not p1_wins_fight(player, boss):
                        losing_costs.add(cost)

    print(max(losing_costs))
