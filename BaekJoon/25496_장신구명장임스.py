P, N = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
result = N
idx = 0
temp = P
while idx < N:
    temp += L[idx]
    if temp >= 200:
        result = idx + 1
        break
    idx += 1
if P == 200:
    result = 0
print(result)
