import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
# N = int(sys.stdin.readline())
# L = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1] * N
for i in range(N):
    while stack and L[i] > L[stack[-1]]:
        result[stack.pop()] = L[i]
    stack.append(i)
print(*result)
