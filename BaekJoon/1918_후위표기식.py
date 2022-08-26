
s = input()
stack = []
result = []
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
top = -1
for i in s:
    if i.isalpha():
        result.append(i)
    elif i == ')':
        while stack[top] != '(':
            result.append(stack.pop())
            top -= 1
        stack.pop()
        top -= 1
    else:
        if not stack:
            stack.append(i)
            top += 1
        elif icp[i] > isp[stack[top]]:
            stack.append(i)
            top += 1
        else:
            while stack and icp[i] <= isp[stack[top]]:
                result.append(stack.pop())
                top -= 1
            stack.append(i)
            top += 1
while stack:
    result.append(stack.pop())
print(''.join(result))
