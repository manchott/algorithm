N = int(input())
L = list(map(int, input().split()))

count, up, down = 1, 1, 1

for i in range(1, len(L)):
    if L[i] - L[i - 1] > 0:
        up += 1
        down = 1
    elif L[i] - L[i - 1] < 0:
        up = 1
        down += 1
    else:
        up += 1
        down += 1
    count = max(up, down, count)
print(count)
