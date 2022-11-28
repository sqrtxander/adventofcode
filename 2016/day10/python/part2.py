from collections import defaultdict

def solve(file):
    with open(file, 'r') as f:
        instructions = [line.split() for line in f.read().splitlines()]
        inital = [instruction for instruction in instructions if instruction[0] == 'value']
        instructions = [instruction for instruction in instructions if instruction[0] != 'value']
    bots = defaultdict(list)
    outputs = defaultdict(list)

    for instruction in inital:
        bots[int(instruction[5])].append(int(instruction[1]))

    while True:
        for instruction in instructions:
            if len(bots[int(instruction[1])]) == 2:
                low = min(bots[int(instruction[1])])
                high = max(bots[int(instruction[1])])
                if instruction[5] == 'output':
                    outputs[int(instruction[6])].append(low)
                else:
                    bots[int(instruction[6])].append(low)
                if instruction[10] == 'output':
                    outputs[int(instruction[11])].append(high)
                else:
                    bots[int(instruction[11])].append(high)
                bots[int(instruction[1])] = []
        if not any(len(chips) == 2 for chips in bots.values()):
            return outputs[0][0] * outputs[1][0] * outputs[2][0]
            


        
if __name__ == '__main__':

    print(solve('../input.in'))
