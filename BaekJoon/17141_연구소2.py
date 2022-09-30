from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 상하좌우
move = ((-1, 0), (1, 0), (0, -1), (0, 1))

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
wall = []
viruses = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            wall.append((i, j))
        elif grid[i][j] == 2:
            viruses.append((i, j))
            grid[i][j] = 0

result = float('inf')
for virus in combinations(viruses, M):
    visited = [[0] * N for _ in range(N)]
    for x, y in virus:
        visited[x][y] = 1
    for x, y in wall:
        visited[x][y] = 1
    Q = deque(virus[:])
    count = M + len(wall)
    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx, ny))
                count += 1
            if count == N ** 2:
                temp = 0
                for i in range(N):
                    temp = max(max(visited[i]), temp)
                result = min(result, temp - 1)
                break

print(result if result != float('inf') else -1)
                



