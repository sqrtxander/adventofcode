if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        subsystem = f.read().splitlines()

    reverse = {')': '(', ']': '[', '}': '{', '>': '<'}
    closing = (')', ']', '}', '>')
    point_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points = 0

    for line in subsystem:
        characters = [line[0]]
        for char in line[1:]:
            if char in closing:
                if reverse[char] == characters[-1]:
                    characters.pop(-1)
                else:
                    points += point_map[char]
                    break
            else:
                characters.append(char)

    print(points)
