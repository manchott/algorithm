N = int(input())
students = [input() for _ in range(N)]
num = 0
for i in range(1, len(students[0]) + 1):
    temp = []
    for student in students:
        temp.append(student[-i:])
    if len(temp) == len(set(temp)):
        num = i
        break
print(num)
