import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))
part_sum = [0] * (N + 1)
for i in range(1, N + 1):
    part_sum[i] = part_sum[i - 1] + L[i - 1]

for i in range(M):
    s, e = map(int, input().split())
    print(part_sum[e] - part_sum[s - 1])