import sys
input = sys.stdin.readline

N = int(input())
P = [input().split() for _ in range(N)]
P.sort(key=lambda x: int(x[0]))
for i in range(N):
    print(*P[i])