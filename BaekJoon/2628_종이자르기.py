r, c = map(int, input().split())
N = int(input())
row = [0]
cross = [0]
for i in range(N):
    way, num = map(int, input().split())
    # 세로로 자르는 선
    if way:
        row.append(num)
    else:
        cross.append(num)
row.append(r)
cross.append(c)
row.sort()
cross.sort()
row_gap = []
cross_gap = []
for i in range(1, len(row)):
    row_gap.append(abs(row[i] - row[i - 1]))
for i in range(1, len(cross)):
    cross_gap.append(abs(cross[i] - cross[i - 1]))
result = 0
for r in row_gap:
    for c in cross_gap:
        result = max(result, r * c)

print(result)