def move_pawn(start, dice):
    return (start + dice - 1) % 10 + 1


def parse(file):
    with open(file, 'r') as f:
        f = f.read().splitlines()
        p1 = int(f[0].split()[-1])
        p2 = int(f[1].split()[-1])

    return p1, p2


def solve(p1, p2):
    game_states = {}

    def count_wins(p1, p2, score_1=0, score_2=0):
        if score_1 >= 21:
            return 1, 0
        elif score_2 >= 21:
            return 0, 1

        wins = [0, 0]

        if (p1, p2, score_1, score_2) in game_states:
            return game_states[(p1, p2, score_1, score_2)]

        for d1 in (1, 2, 3):
            for d2 in (1, 2, 3):
                for d3 in (1, 2, 3):
                    new_p1 = move_pawn(p1, d1 + d2 + d3)
                    new_s1 = score_1 + new_p1

                    x1, y1 = count_wins(p2, new_p1, score_2, new_s1)
                    wins[0] += y1
                    wins[1] += x1
        game_states[(p1, p2, score_1, score_2)] = wins
        return wins

    return max(count_wins(p1, p2, 0, 0))


if __name__ == '__main__':
    EXPECTED = 444356092776315
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))
