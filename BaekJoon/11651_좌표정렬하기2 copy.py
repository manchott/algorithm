import sys
input = sys.stdin.readline

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
L.sort(key=lambda x: (x[1], x[0]))
print()
for i in range(N):
    print(*L[i])