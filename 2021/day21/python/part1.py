class Player:
    def __init__(self, start):
        self.space = start
        self.score = 0

    def move_pawn(self, dice):
        self.space = self.space + dice
        self.space = (self.space - 1) % 10 + 1
        self.score += self.space


def parse(file):
    with open(file, 'r') as f:
        f = f.read().splitlines()
        p1 = int(f[0].split()[-1])
        p2 = int(f[1].split()[-1])

    return p1, p2


def solve(p1, p2):
    def roll_dice():
        result = 0
        for _ in range(3):
            s = dice.pop(0)
            dice.append(s)
            result += s
        return result


    dice = list(range(1, 101))
    dice_rolled = 0
    player1 = Player(p1)
    player2 = Player(p2)
    while True:
        player1.move_pawn(roll_dice())
        dice_rolled += 3
        if player1.score >= 1000:
            return player2.score * dice_rolled
        player2.move_pawn(roll_dice())
        dice_rolled += 3
        if player2.score >= 1000:
            return player1.score * dice_rolled


if __name__ == '__main__':

    EXPECTED = 739785
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))
