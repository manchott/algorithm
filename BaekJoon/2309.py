L = []
for i in range(9):
    L.append(int(input()))

for i in range(9):
    for j in range(i + 1, 9):
        total = sum(L)
        total -= L[i] + L[j]

        if total == 100:
            L.remove(L[j])
            L.remove(L[i])
            break
    if len(L) == 7:
        break
L.sort()
for i in L:
    print(i)
