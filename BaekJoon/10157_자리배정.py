# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())
seat = [[0] * C for _ in range(R)]
x, y = R - 1, 0
seat[x][y] = 1
idx = 0
for i in range(2, K + 1):
    if i > C * R:
        print(0)
        exit()
    nx, ny = x + dx[idx], y + dy[idx]
    if 0 <= nx < R and 0 <= ny < C and not seat[nx][ny]:
        x, y = nx, ny
    else:
        idx = (idx + 1) % 4
        x, y = x + dx[idx], y + dy[idx]
    seat[x][y] = i
print(y + 1, R - x)
