import time

game_list = [11, 18, 0, 20, 1, 7, 16]
game_dict = {n: i for i, n in enumerate(game_list)}

t = time.perf_counter()


def next_num(prev):
    if prev not in game_dict:
        return 0
    else:
        return len(game_list) - game_dict[prev] - 1


def nth_elem(n):
    while len(game_list) < n:
        game_list.append(next_num(game_list[-1]))
        game_dict[game_list[-2]] = len(game_list) - 2
    return game_list[n - 1]


print(nth_elem(2020))
print(nth_elem(30000000))
print(f'executed in {time.perf_counter()-t} seconds')