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


if __name__ == '__main__':
    names = set()
    stats = dict()
    with open('../input.txt') as f:
        for line in f:
            n, s, t, r = re.findall(r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)[0]
            names.add(n)
            stats[n] = (int(s), int(t), int(r))

    reindeer = [Reindeer(stats[r][0], stats[r][1], stats[r][2]) for r in names]

    distances = [r.calculate_distance(2503) for r in reindeer]

    print(max(distances))
