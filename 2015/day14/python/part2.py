import re


class Reindeer:
    def __init__(self, s, t, r):
        self.speed = s
        self.move_time = t
        self.rest_time = r
        self.points = 0
        self.prev_distance = 0

    def get_next_distance(self, time):
        if 0 != time % (self.move_time + self.rest_time) <= self.move_time:
            self.prev_distance += self.speed
        return self.prev_distance


if __name__ == '__main__':
    names = set()
    stats = dict()
    with open('../input.txt') as f:
        for line in f:
            n, s, t, r = re.findall(r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)[0]
            names.add(n)
            stats[n] = (int(s), int(t), int(r))

    reindeer = [Reindeer(stats[r][0], stats[r][1], stats[r][2]) for r in names]

    for time in range(1, 2503+1):
        winners = []

        dist = [r.get_next_distance(time) for r in reindeer]
        for i in range(len(dist)):
            if dist[i] == max(dist):
                winners.append(reindeer[i])

        for r in winners:
            r.points += 1

    print(max(r.points for r in reindeer))