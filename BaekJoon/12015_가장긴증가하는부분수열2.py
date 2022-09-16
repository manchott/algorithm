N = int(input())
L = list(map(int, input().split()))
stack = [L[0]]

def binary(target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if L[mid] <= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1 
    return result
        

for i in range(1, N):
    if stack[-1] < L[i]:
        stack.append(L[i])
    else:
        result = binary(L[i], 0, len(stack) - 1)
# 보류