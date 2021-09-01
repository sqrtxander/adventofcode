import re


class Reindeer:
    def __init__(self, s, t, r):
        self.speed = s
        self.move_time = t
        self.rest_time = r
        self.points = 0
        self.prev_distance = 0

    def calculate_distance(self, time):
        distance = 0
        for t in range(1, time+1):
            if 0 != t % (self.move_time + self.rest_time) <= self.move_time:
                distance += self.speed
        return distance

    def get_next_distance(self, time):
        if 0 != time % (self.move_time + self.rest_time) <= self.move_time:
            self.prev_distance += self.speed
        return self.prev_distance


names = set()
stats = dict()
with open('inputs/input14.txt') as f:
    for line in f:
        n, s, t, r = re.findall(r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)[0]
        names.add(n)
        stats[n] = (int(s), int(t), int(r))


reindeer = [Reindeer(stats[r][0], stats[r][1], stats[r][2]) for r in names]

distances = [r.calculate_distance(2503) for r in reindeer]

print(max(distances))

for time in range(1, 2503+1):
    winners = []

    dist = [r.get_next_distance(time) for r in reindeer]
    for i in range(len(dist)):
        if dist[i] == max(dist):
            winners.append(reindeer[i])

    for r in winners:
        r.points += 1

print(max(r.points for r in reindeer))
