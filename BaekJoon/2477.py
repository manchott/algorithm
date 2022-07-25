n = int(input())
side1 = []
side2 = []
side = []
for i in range(6):
    x, y = map(int, input().split())
    side.append(y)

if i % 2:
    side1.append(y)
else:
    side2.append(y)

t = max(side1)
j = max(side2)
x, y = side1.index(t), side2.index(j)
side1.pop(y)
side2.pop(x)
print(t, j, x, y)


a = abs(side1[1] - side1[0])
b = abs(side2[1] - side2[0])

print(t, j, x, y, a, b)
result = (t * j) - (a * b)

print(result * n)
# 1 동
# 2 서
# 3 남
# 4 북
