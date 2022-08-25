N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]
grid = [[0, 0, 0] for _ in range(N)]
grid[0] = color[0]
for i in range(1, N):
    grid[i][0] = color[i][0] + min(grid[i - 1][1], grid[i - 1][2])
    grid[i][1] = color[i][1] + min(grid[i - 1][0], grid[i - 1][2])
    grid[i][2] = color[i][2] + min(grid[i - 1][1], grid[i - 1][0])

print(min(grid[N - 1]))
