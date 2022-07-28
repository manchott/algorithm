T = int(input())
for i in range(T):
    grid = []
    N = int(input())
    result = [[] for i in range(N)]
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    print(f'#{i + 1}')
    for x in range(N):
        for y in range(N):
            print(grid[N - y - 1][x], end='')
        print(' ', end='')
        for y in range(N):
            print(grid[N - x - 1][N - y - 1], end='')
        print(' ', end='')
        for y in range(N):
            print(grid[y][N - x - 1], end='')
        print('\n', end='')
