def magnitude(num):
    if type(num) == int:
        return num
    elif type(num) == list:
        return 3 * magnitude(num[0]) + 2 * magnitude(num[1])
    else:
        raise


def find_explode(num, depth=0):
    if type(num) == list:
        if depth == 4:
            return True
        for i in num:
            e = find_explode(i, depth+1)
            if e:
                return i
    return False


def explode(num, depth=0):
    if type(num) == list:
        if depth >= 4:
            return num
        for i in num:
            e = explode(i, depth+1)
            if e is not None:
                return explode(i, depth+1)




def solve(file):
    with open(file, 'r') as f:
        snail_nums = [eval(line) for line in f.read().splitlines()]
    total = []
    for snail_num in snail_nums:
        total += [snail_num]
    return magnitude(total)



if __name__ == '__main__':

    # EXPECTED = 4140
    # test = solve('../test.in')
    # assert test == EXPECTED, f'Got {test} should be {EXPECTED}'
    # print(solve('../input.in'))
    # print(solve([[1,2], [[3,4],5]]))

    # print(magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]))

    print(find_explode([[[[0,7],4],[7,[[8,4],9]]],[1,1]]))
    print(find_explode([[[[0,7],4],[15,[0,13]]],[1,1]]))
    # print(explode([[[[[9,8],1],2],3],4]))
    # print(explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]))
    # print(explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]))
    # print(str([1, [2, 3]]))