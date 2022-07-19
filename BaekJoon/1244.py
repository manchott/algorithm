n = int(input())
lights = list(map(int, input().split()))
lights.insert(0, 0)    # 본인이 받은 숫자 = 스위치 숫자를 위해 맨 앞에 [0] 삽입
students = int(input())

for _ in range(students):
    gender, switch = map(int, input().split())
    if gender == 1:   # 남학생인 경우
        for i in range(switch, n + 1, switch):
            lights[i] = 1 - lights[i]   # 1이면 0으로, 0이면 1로 바꿈

    else:   # 여학생인 경우
        start, end = switch, switch
        while start > 1 and end < n:
            if lights[start - 1] == lights[end + 1]:
                start -= 1
                end += 1
            else:
                break
        for i in range(start, end + 1):
            lights[i] = 1 - lights[i]   # 1이면 0으로, 0이면 1로 바꿈

for i in range(1, n + 1):
    print(lights[i], end=" ")
    if i % 20 == 0:
        print()
