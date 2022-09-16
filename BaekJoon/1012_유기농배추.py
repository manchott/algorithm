import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    visited[x][y] = 1
    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and farm[nx][ny]:
            dfs(nx, ny)


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)

