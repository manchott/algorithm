import sys
input = sys.stdin.readline

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
result = [0] * M
Nlist.sort()
for i in range(M):
    start, end, target = 0, N - 1, Mlist[i]
    while start <= end:
        mid = (start + end) // 2
        if Nlist[mid] == target:
            result[i] = 1
            break
        elif Nlist[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
print(*result)
