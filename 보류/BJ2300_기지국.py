# 포기!!!!!!!!!!

N = int(input())
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
B.sort()
B.append([0, 0])
count = 0
start_x, start_y = B[0][0], B[0][1]
idx = 1

while True:
    # if idx > 7:
    #     count += max(abs(start_y), abs(y), abs(x - start_x))
    x, y = B[idx][0], B[idx][1]
    # 기준점의 y축과 반대쪽에 있고, 그 다음 점보다 더 큰값이라면
    if abs(y) >= abs(start_y):
        count += max(abs(start_y), abs(y), abs(x - start_x))
        start_x, start_y = B[idx + 1][0], B[idx + 1][1]
    if y == 0:
        count += max(abs(start_y), abs(y), abs(x - start_x))
        break
    idx += 1
print(count)
