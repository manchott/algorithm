N, K = map(int, input().split())
temp = list(map(int, input().split()))
temp_sum = [temp[0]]
temp_serial = []
for i in range(1, N):
    temp_sum.append(temp_sum[i - 1] + temp[i])
temp_sum.insert(0, 0)
for i in range(N - K + 1):
    temp_serial.append(temp_sum[i + K] - temp_sum[i])
print(max(temp_serial))
