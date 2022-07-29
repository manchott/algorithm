N, K = map(int, input().split())
temp = list(map(int, input().split()))
temp_sum = [temp[0]]
temp_gap_K = []
for i in range(1, N):
    temp_sum.append(temp_sum[i - 1] + temp[i])
temp_sum.insert(0, 0)
for i in range(N - K):
    temp_gap_K.append(temp_sum[i + K] - temp_sum[i])
print(temp_sum)
print(temp_gap_K)
print(max(temp_gap_K))
