from collections import Counter


def parse(file):
    with open(file, 'r') as f:
        polymer, pairs = f.read().split('\n\n')
        polymer_pairs = Counter([a + b for a, b in zip(polymer, polymer[1:])])

        pairs = pairs.split('\n')
        replacements = {}
        for i, line in enumerate(pairs):
            a, b = line.split(' -> ')
            replacements[a] = b

        letter_count = Counter(polymer)

    return polymer_pairs, replacements, letter_count


def solve(polymer_pairs, replacements, letter_count):
    new_polymer_pairs = polymer_pairs.copy()

    for _ in range(40):
        for rep in replacements:
            a, b = rep[0], rep[1]
            c = replacements[rep]
            count = polymer_pairs[rep]
            new_polymer_pairs[a + c] += count
            new_polymer_pairs[c + b] += count
            new_polymer_pairs[rep] -= count
            letter_count[c] += count
        polymer_pairs = new_polymer_pairs.copy()

    return max(letter_count.values()) - min(letter_count.values())


if __name__ == '__main__':

    EXPECTED = 2188189693529
    test = solve(*parse('../test.in'))
    assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    print(solve(*parse('../input.in')))