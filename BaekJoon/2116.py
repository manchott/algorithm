n = int(input())
storage = []

for _ in range(n):
    storage.append(list(map(int, input().split())))
storage.sort()
start = storage[0][1]
end = storage[-1][1]
max_height = max(s[1] for s in storage)     # 가장 높은 기둥

# print(start, end, max_height)
result = 0
fmh = 0
lmh = 0
pnum, pheight = storage[0][0], storage[0][1]
for i in range(1, n):
    if pheight == max_height:
        break
    print(i)
    cnum, cheight = storage[i][0], storage[i][1]
    if cheight <= max_height:
        if cheight < pheight:  # 이전것보다 높이가 낮다면 제외
            continue
        else:
            result += (cnum - pnum) * pheight
            pnum, pheight = cnum, cheight
    if cheight == max_height:
        fmh = i
        break

pnum, pheight = storage[-1][0], storage[-1][1]
for i in range(n - 2, 0, -1):
    print("i:", i)
    cnum, cheight = storage[i][0], storage[i][1]
    if cheight <= max_height:
        if cheight < pheight:  # 이전것보다 높이가 낮다면 제외
            continue
        else:
            print("else")
            result += (pnum - cnum) * pheight
            pnum, pheight = cnum, cheight
    if cheight == max_height:
        lmh = i
        break
result += (lmh - fmh + 1) * max_height

print(result)

'''
4
8 10
11 4
13 6
15 8
'''
