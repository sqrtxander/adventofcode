from collections import Counter


if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        polymer, pairs = f.read().split('\n\n')

        polymer_pairs = Counter([a + b for a, b in zip(polymer, polymer[1:])])

        pairs = pairs.split('\n')
        replacements = {}
        for i, line in enumerate(pairs):
            a, b = line.split(' -> ')
            replacements[a] = b

    new_polymer_pairs = polymer_pairs.copy()
    letter_count = Counter(polymer)
    for _ in range(10):
        for rep in replacements:
            a, b = rep[0], rep[1]
            c = replacements[rep]
            count = polymer_pairs[rep]
            new_polymer_pairs[a + c] += count
            new_polymer_pairs[c + b] += count
            new_polymer_pairs[rep] -= count
            letter_count[c] += count
        polymer_pairs = new_polymer_pairs.copy()

    print(max(letter_count.values()) - min(letter_count.values()))