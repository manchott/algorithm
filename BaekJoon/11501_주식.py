import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    max_num = profit = 0
    for i in range(N - 1, -1, -1):
        if L[i] > max_num:
            max_num = L[i]
        else:
            profit += max_num - L[i]
    print(profit)
