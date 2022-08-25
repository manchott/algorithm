N = int(input())
B = [[0, 0]]
for _ in range(N):
    B.append(list(map(int, input().split())))
B.sort()
dp = [float('inf')] * (N + 1)
for i in range(1, N + 1):
    h = abs(B[i][1])
    for j in range(i - 1, -1, -1):
