for i in range(6, 26):
    i = str(i).zfill(2)
    f = open(f'inputs/input{i}.txt', 'w')
    f.close()
    f = open(f'day{i}.py', 'w')
    f.close()
