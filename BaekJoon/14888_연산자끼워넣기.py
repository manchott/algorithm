import sys
input = sys.stdin.readline

def BT(idx, calc):
    # print(idx, calc)
    global min_calc, max_calc
    if idx == N:
        min_calc = min(min_calc, calc)
        max_calc = max(max_calc, calc)
        return
    for i in range(N - 1):
        if not visited[i]:
            visited[i] = idx
            if operator[i] == '+':
                BT(idx + 1, calc + nums[idx])
            elif operator[i] == '-':
                BT(idx + 1, calc - nums[idx])
            elif operator[i] == '*':
                BT(idx + 1, calc * nums[idx])
            elif operator[i] == '/':
                if calc < 0 and nums[idx] > 0:
                    BT(idx + 1, -(abs(calc) // nums[idx]))
                else:
                    BT(idx + 1, calc // nums[idx])
            visited[i] = 0


N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
operator = '+' * operator[0] + '-' * operator[1] + '*' * operator[2] + '/' * operator[3]
visited = [0] * (N - 1)
min_calc = float('inf')
max_calc = -float('inf')
BT(1, nums[0])
print(max_calc)
print(min_calc)