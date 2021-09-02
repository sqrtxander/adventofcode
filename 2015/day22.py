class Player:
    def __init__(self, health, mana):
        self.health_init = health
        self.health = self.health_init
        self.mana_init = mana
        self.mana = self.mana_init
        self.armor = 0
        self.timer = []

    def use_spell(self, spell, opp):
        if spell == 'Magic Missile':
            self.mana -= 53
            opp.health -= 4
        elif spell == 'Drain':
            self.mana -= 73
            opp.health -= 2
            self.health += 2
        elif spell == 'Shield':
            self.mana -= 113
            self.armor += 7
            self.timer.append(('Shield', 6))
        elif spell == 'Poison':
            self.mana -= 173
            self.timer.append(('Poison', 6))
        elif spell == 'Recharge':
            self.mana -= 229
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


class Boss:
    def __init__(self, health, dam):
        self.health_init = health
        self.health = self.health_init
        self.damage = dam

    def reset(self):
        self.health = self.health_init

    def attack(self, opp):
        hit = self.health - opp.armor
        hit = hit if hit >= 1 else 1
        opp.health -= hit

        
with open('inputs/input22.txt', 'r') as f:
    boss_hp, boss_dam = [int(x.split(': ')[-1]) for x in f.readlines()]

print(boss_hp, boss_dam)


boss = Boss(boss_hp, boss_dam)
player = Player(50, 500)


