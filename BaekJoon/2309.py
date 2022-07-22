L = []
for i in range(9):
    L.append(int(input()))

for i in range(9):
    for j in range(i + 1, 9):
        total = sum(L)
        total -= L[i] + L[j]
        print(i, j)

        if total == 100:
            L.remove(L[j])
            L.remove(L[i])
            break
    if len(L) == 7:
        break

for i in range(7):
    if i == 6:
        print(sorted(L)[i])
    else:
        print(sorted(L)[i], end=' ')
