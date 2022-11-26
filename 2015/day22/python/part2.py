def solve(file):
    def player_turn(game, spell):
        if spell == 'Magic Missile':
            game['boss_hp'] = game['boss_hp'] - 4
        
        elif spell == 'Drain':
            game['boss_hp'] = game['boss_hp'] - 2
            game['player_hp'] = game['player_hp'] + 2
        
        elif spell == 'Shield':
            game['shield_timer'] = 6
            game['player_armor'] = game['player_armor'] + 7
        
        elif spell == 'Poison':
            game['poison_timer'] = 6
        
        elif spell == 'Recharge':
            game['recharge_timer'] = 5
        game['player_mana'] = game['player_mana'] - SPELL_COSTS[spell]

    def boss_turn(game):
        dmg = max(1, game['boss_dmg'] - game['player_armor'])
        game['player_hp'] -= dmg

    def apply_effects(game):
        if game['shield_timer']:
            game['shield_timer'] = game['shield_timer'] - 1
            if game['shield_timer'] == 0:
                game['player_armor'] = 0

        if game['poison_timer']:
            game['boss_hp'] = game['boss_hp'] - 3
            game['poison_timer'] = game['poison_timer'] - 1

        if game['recharge_timer']:
            game['player_mana'] = game['player_mana'] + 101
            game['recharge_timer'] = game['recharge_timer'] - 1

    def is_over_and_min(game, min_mana):
        if game['player_hp'] <= 0:
            return True, min_mana
        if game['boss_hp'] <= 0:
            return True, min(min_mana, game['mana_spent'])
        return False, min_mana

    def try_all_games(games, min_mana):
        new_games = []
        for game in games:

            game['player_hp'] -= 1
            over, min_mana = is_over_and_min(game, min_mana)
            if over:
                continue

            apply_effects(game)
            endgame, min_mana = is_over_and_min(game, min_mana)
            if endgame:
                continue

            min_mana = try_all_spells(game, min_mana, new_games)

        return new_games, min_mana

    def try_all_spells(game, min_mana, new_games):
        castable_spells = [spell for spell, cost in SPELL_COSTS.items()
                           if cost <= game['player_mana']]
        if game['shield_timer'] and 'Shield' in castable_spells:
            castable_spells.remove('Shield')
        if game['poison_timer'] and 'Poison' in castable_spells:
            castable_spells.remove('Poison')
        if game['recharge_timer'] and 'Recharge' in castable_spells:
            castable_spells.remove('Recharge')

        for spell in castable_spells:

            sub_game = game.copy()
            sub_game['spells_cast'] = list(sub_game['spells_cast']) + [spell]
            sub_game['mana_spent'] = sub_game['mana_spent']+SPELL_COSTS[spell]

            player_turn(sub_game, spell)
            endgame, min_mana = is_over_and_min(sub_game, min_mana)
            if endgame:
                continue

            if sub_game['mana_spent'] > min_mana:
                continue

            apply_effects(sub_game)
            endgame, min_mana = is_over_and_min(sub_game, min_mana)
            if endgame:
                continue

            boss_turn(sub_game)
            endgame, min_mana = is_over_and_min(sub_game, min_mana)
            if endgame:
                continue

            new_games.append(sub_game)
        return min_mana

    SPELL_COSTS = {'Magic Missile': 53,
                   'Drain': 73,
                   'Shield': 113,
                   'Poison': 173,
                   'Recharge': 229}

    with open(file, 'r') as f:
        boss_hp, boss_dmg = [int(x.split(': ')[-1]) for x in f.readlines()]

        game = {'player_hp': 50,
                'player_mana': 500,
                'player_armor': 0,

                'boss_hp': boss_hp,
                'boss_dmg': boss_dmg,

                'shield_timer': 0,
                'poison_timer': 0,
                'recharge_timer': 0,

                'spells_cast': [],
                'mana_spent': 0}

        games = [game]
        min_mana = float('inf')
        while len(games):
            games, min_mana = try_all_games(games, min_mana)
        return min_mana


if __name__ == '__main__':

    print(solve('../input.in'))
