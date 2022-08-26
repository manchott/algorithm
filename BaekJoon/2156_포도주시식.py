N = int(input())
wine = [int(input()) for _ in range(N)]
count = [0]
for i in range(N):
    if i == 0:
        count.append(wine[0])
    elif i == 1:
        count.append(wine[0] + wine[1])
    else:
        count.append(max(count[-1], wine[i] + count[-2],
                     wine[i] + wine[i - 1] + count[-3]))
print(count)
print(count[-1])
