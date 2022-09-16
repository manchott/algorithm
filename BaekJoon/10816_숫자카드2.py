import sys
input = sys.stdin.readline

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
Mdict = {num: 0 for num in Mlist}
result = [0] * M
for i in range(N):
    if Nlist[i] in Mdict.keys():
        Mdict[Nlist[i]] += 1
for i in range(M):
    result[i] = Mdict[Mlist[i]]
print(*result)
