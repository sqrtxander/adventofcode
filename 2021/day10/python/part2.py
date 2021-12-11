def score_incomplete(line):
    score = 0
    point_map = {')': 1, ']': 2, '}': 3, '>': 4}
    for char in line:
        score *= 5
        score += point_map[char]
    return score


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        subsystem = [line for line in f.read().splitlines()]

    reverse = {')': '(', ']': '[', '}': '{', '>': '<'}
    forward = {o: c for c, o in zip(reverse.keys(), reverse.values())}
    closing = (')', ']', '}', '>')
    completing = []

    for line in subsystem:
        characters = [line[0]]
        for char in line[1:]:
            if char in closing:
                if reverse[char] == characters[-1]:
                    characters.pop(-1)
                else:
                    break
            else:
                characters.append(char)
        else:
            completing.append([forward[char] for char in reversed(characters)])

    scores = [score_incomplete(line) for line in completing]
    scores.sort()
    print(scores[len(completing)//2])