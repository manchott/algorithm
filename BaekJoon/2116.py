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
print(storage)
for i in range(1, n + 1):
    print("i: ", i)
    cnum, cheight = storage[i][0], storage[i][1]
    pnum, pheight = storage[i - 1][0], storage[i - 1][1]
    print("c num, height", cnum, cheight)
    if cheight <= max_height:
        if cheight < pheight:  # 이전것보다 높이가 낮다면 제외
            continue
        else:
            result += (cnum - pnum) * pheight
            print('rr: ', result)
    if cheight == max_height:
        fmh = i
        break

for i in range(n - 2, 0, -1):
    print("i: ", i)
    cnum, cheight = storage[i][0], storage[i][1]
    pnum, pheight = storage[i + 1][0], storage[i + 1][1]
    if cheight <= max_height:
        if cheight < pheight:  # 이전것보다 높이가 낮다면 제외
            continue
        else:
            result += (pnum - cnum) * pheight
    if cheight == max_height:
        lmh = i
        break

    print(0)
result += (lmh - fmh + 1) * max_height

print(result)
