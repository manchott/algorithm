import sys
input = sys.stdin.readline

N = int(input())
count = [[0] * 10 for _ in range(100)]
for i in range(1, 10):
    count[0][i] = 1
for i in range(1, N):
    count[i][0] = count[i - 1][1]
    for j in range(1, 9):
        count[i][j] = (count[i - 1][j - 1] + count[i - 1][j + 1])
    count[i][9] = count[i - 1][8]

target = count[N - 1]
target_sum = sum(target) % 1000000000
print(target_sum)