N = int(input())
L = list(map(int, input().split()))
up = [1] * N
down = [1] * N
for i in range(1, N):
    for j in range(i):
        if L[i] > L[j]:
            up[i] = max(up[i], up[j] + 1)
            
L.reverse()
for i in range(1, N):
    for j in range(i):
        if L[i] > L[j]:
            down[i] = max(down[i], down[j] + 1)
down.reverse()
result = [x + y for x, y in zip(up, down)]
print(max(result) - 1)