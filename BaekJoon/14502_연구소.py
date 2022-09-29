from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 상하좌우
move = ((-1, 0), (1, 0), (0, -1), (0, 1))

def BFS():
    Q = deque()
    for i in virus:
        Q.append(i)
    while Q:
        x, y = Q.popleft()
        visited[x][y] = 1
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and (nx, ny) not in wall:
                visited[nx][ny] = 1
                Q.append((nx, ny))

    
def count():
    num = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                num += 1
    return num



N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
blank = []
wall = []
virus = []
result = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            blank.append((i, j))
        elif grid[i][j] == 1:
            wall.append((i, j))
        elif grid[i][j] == 2:
            virus.append((i, j))
comb = list(combinations(blank, 3))
for a, b, c in comb:
    visited = [[0] * M for _ in range(N)]
    visited[a[0]][a[1]] = 1
    visited[b[0]][b[1]] = 1
    visited[c[0]][c[1]] = 1
    BFS()
    result = max(result, count())
print(result - len(wall))
