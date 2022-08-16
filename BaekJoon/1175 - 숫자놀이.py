M, N = map(int, input().split())
alpha = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
result = []
for i in range(M, N + 1):
    temp = []
    while i > 0:
        num = i // 10
        temp.append(alpha[num])
        i %= 10
    result.append(' '.join(temp))
print(*sorted(result))
