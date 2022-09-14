N = int(input())
bag5 = bag3 = 0
temp = N
while temp > 0:
    if temp < 15:
        if temp % 3 == 0:
            bag3 += temp // 3
            temp = 0
        else:
            bag5 += 1
            temp -= 5
    else:
        bag5 += 1
        temp -= 5
print(-1) if (bag5 * 5) + (bag3 * 3) != N else print(bag5 + bag3)