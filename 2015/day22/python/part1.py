import itertools


class Player:
    def __init__(self, health, mana):
        self.health_init = health
        self.health = self.health_init
        self.mana_init = mana
        self.mana = self.mana_init
        self.armor = 0
        self.timer = []
        self.mana_used = 0
        self.spell_costs = {'Magic Missile': 53, 'Drain': 73, 'Shield': 113, 'Poison': 173, 'Recharge': 229}

    def use_spell(self, spell, opp):
        if self.mana < self.spell_costs[spell]:
            return
        if spell in [eff for eff, _ in self.timer]:
            return
        if spell == 'Magic Missile':
            self.mana -= self.spell_costs[spell]
            self.mana_used += self.spell_costs[spell]
            opp.health -= 4
        elif spell == 'Drain':
            self.mana -= self.spell_costs[spell]
            self.mana_used += self.spell_costs[spell]
            opp.health -= 2
            self.health += 2
        elif spell == 'Shield':
            self.mana -= self.spell_costs[spell]
            self.mana_used += self.spell_costs[spell]
            self.armor += 7
            self.timer.append(('Shield', 6))
        elif spell == 'Poison':
            self.mana -= self.spell_costs[spell]
            self.mana_used += self.spell_costs[spell]
            self.timer.append(('Poison', 6))
        elif spell == 'Recharge':
            self.mana -= self.spell_costs[spell]
            self.mana_used += self.spell_costs[spell]
            self.timer.append(('Recharge', 5))

    def manage_effects(self, opp):

        for effect, time in self.timer:
            if effect == 'Shield' and time == 0:
                self.armor -= 7
            elif effect == 'Poison' and time > 0:
                opp.health -= 3
            elif effect == 'Recharge' and time > 0:
                self.mana += 101

        self.timer = [(eff, tim - 1) for eff, tim in self.timer if tim > 0]

    def reset(self):
        self.timer = []
        self.armor = 0
        self.health = self.health_init
        self.mana = self.mana_init
        self.mana_used = 0


class Boss:
    def __init__(self, health, dam):
        self.health_init = health
        self.health = self.health_init
        self.damage = dam

    def reset(self):
        self.health = self.health_init

    def attack(self, opp):
        hit = self.damage - opp.armor
        hit = hit if hit >= 1 else 1
        opp.health -= hit


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        boss_hp, boss_dam = [int(x.split(': ')[-1]) for x in f.readlines()]

    print(boss_hp, boss_dam)
    spells = ('Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge')

    boss = Boss(boss_hp, boss_dam)
    player = Player(10, 250)

    min_mana = float('inf')
    combos = list(itertools.product(spells, repeat=5))
    for spell_order in combos:
        player.reset()
        boss.reset()
        # spell_order = ('Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile')
        for spell in spell_order:
            player.manage_effects(boss)
            player.use_spell(spell, boss)
            if boss.health <= 0:
                if player.mana_used < min_mana:
                    min_mana = player.mana_used
                    path = spell_order
                break

            player.manage_effects(boss)
            if boss.health <= 0:
                if player.mana_used < min_mana:
                    min_mana = player.mana_used
                    path = spell_order
                break

            boss.attack(player)
            if player.health <= 0:
                break

    print(min_mana)
    print(path)
