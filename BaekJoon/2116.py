n = int(input())
dlist = []
for _ in range(n):
    dlist.append(list(map(int, input().split())))

# 마주보는 면을 나타내는 딕셔너리
pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}


def side_max(die, idx):
    side_idx = [0, 1, 2, 3, 4, 5]

    side_idx.remove(idx)
    side_idx.remove(pair[idx])
    max_num = max([die[a] for a in side_idx])
    return max_num


max_sum = 0
for i in range(6):
    i_sum = 0
    bottom_idx = i
    top_idx = dlist[0][pair[i]]

    i_sum += side_max(dlist[0], bottom_idx)
    for die in dlist[1:]:
        bottom_idx = die.index(top_idx)
        i_sum += side_max(die, bottom_idx)
        top_idx = die[pair[bottom_idx]]
    max_sum = i_sum if i_sum > max_sum else max_sum

print(max_sum)
