n = int(input())
storage = []

for _ in range(n):
    storage.append(list(map(int, input().split())))

# 위치 순으로 정렬
storage.sort(key=lambda x: x[0])

# 가장 높은 기둥의 높이
max_idx = storage.index(max(storage, key=lambda x: x[1]))
max_height = storage[max_idx][1]

# 최대 넓이
storage_area = max_height * (storage[-1][0] - storage[0][0] + 1)

# 앞에서부터 max_height 기둥까지 반복하며 필요 없는 부분 뺴기
idx = storage[0][0]
height = storage[0][1]
for i in range(1, max_idx + 1):
    if storage[i][1] > height:
        storage_area -= (storage[i][0] - storage[0][0]
                         ) * (storage[i][1] - height)
        idx = storage[i][0]
        height = storage[i][1]
    else:
        continue

# 뒤에서부터 max_height 기둥까지 반복하며 필요 없는 부분 뺴기
idx = storage[-1][0]
height = storage[-1][1]
for i in range(n - 2, max_idx - 1, -1):
    if storage[i][1] > height:
        storage_area -= (storage[-1][0] - storage[i]
                         [0]) * (storage[i][1] - height)
        idx = storage[i][0]
        height = storage[i][1]
    else:
        continue

print(storage_area)
