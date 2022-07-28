n = int(input())
grid = [[0 for col in range(100)] for row in range(100)]
count = 0
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            if grid[j][k] == 0:
                grid[j][k] = 1
                count += 1
            else:
                continue


print(count)
