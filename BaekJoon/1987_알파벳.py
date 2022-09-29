# 상하좌우
move = ((-1, 0), (1, 0), (0, -1), (0, 1))

def DFS(x, y, count):
    global answer
    answer = max(answer, count)
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] not in visited:
            visited.add(grid[nx][ny])
            DFS(nx, ny, count + 1)
            visited.remove(grid[nx][ny])


R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
visited = {grid[0][0]}

answer = 0
DFS(0, 0, 1)
print(answer)