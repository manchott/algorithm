import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
grid = [list(input()) for _ in range(N)]
visited_c = [[0]*N for _ in range(N)]
visited_b = [[0]*N for _ in range(N)]
count_c = count_b = 0

def dfs(x, y, visited, color):
    visited[x][y] = 1
    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and grid[nx][ny] in color:
                dfs(nx, ny, visited, color)


for i in range(N):
    for j in range(N):
        if not visited_c[i][j]:
            color = [grid[i][j]]
            count_c += 1
            dfs(i, j, visited_c, color)
        if not visited_b[i][j]:
            color = []
            if grid[i][j] in ['R', 'G']:
                color = ['R', 'G']
            else:
                color = ['B']
            count_b += 1
            dfs(i, j, visited_b, color)
print(count_c, count_b)
