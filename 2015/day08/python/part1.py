if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    sum_str_len = sum(len(x) for x in data)
    sum_str_memory = sum(len(eval(x)) for x in data)

    print(sum_str_len - sum_str_memory)
