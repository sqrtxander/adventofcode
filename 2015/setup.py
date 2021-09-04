import os

for day in range(1, 26):
    try:
        os.mkdir('day'+str(day).zfill(2))
        os.mkdir('day'+str(day).zfill(2)+'/python')
        open('day'+str(day).zfill(2)+'/input.txt', 'w')
        open('day'+str(day).zfill(2)+'/python/part1.py', 'w')
        open('day'+str(day).zfill(2)+'/python/part2.py', 'w')
    except OSError:
        print('failed')
    else:
        print('success')