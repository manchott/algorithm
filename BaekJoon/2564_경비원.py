M, N = map(int, input().split())
S = int(input())
stores = []
d_num = 0
for i in range(S + 1):
    direction, num = map(int, input().split())
    temp = 0
    # 상
    if direction == 1:
        temp = num
    # 하
    elif direction == 2:
        temp = 2 * M + N - num
    # 좌
    elif direction == 3:
        temp = 2 * (M + N) - num
    # 우
    else:
        temp = M + num
    # 동근이라면 따로 저장
    if i == S:
        d_num = temp
    # 상점이라면 상점 리스트에 저장
    else:
        stores.append(temp)
result = 0
for store in stores:
    result += min(abs(d_num - store), abs(2 * (M + N) - d_num + store), abs(2 * (M + N) + d_num - store))
print(result)