melon = int(input())
side1 = []
side2 = []
side = []
for i in range(6):
    x, y = map(int, input().split())
    side.append(y)
side1_max = max(side[::2])
side2_max = max(side[1::2])
side1_max_idx = side.index(side1_max)
side2_max_idx = side.index(side2_max)

little_side1 = abs(side[(side1_max_idx + 1) % 6] - side[side1_max_idx - 1])
little_side2 = abs(side[(side2_max_idx + 1) % 6] - side[side2_max_idx - 1])
result = (side1_max * side2_max) - (little_side1 * little_side2)
print(result * melon)
