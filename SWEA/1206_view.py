# 1206_view
# 220808

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10 + 1):
    T = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    # 각 빌딩을 돌며 좌우 간격을 확인한다
    for i in range(2, T - 2):
        house = buildings[i]    # 모든 세대가 전망권이 확보되어 있다고 가정
        for j in [-2, -1, 1, 2]:
            gap = buildings[i] - buildings[i + j]
            # 만약 좌우 2칸 이내의 빌딩이 전망권을 해친다면 전망권이 보이는 세대를 0으로 지정, for문 break
            if gap < 0:
                house = 0
                break
            # 그렇지 않다면 전망권이 보이는 세대 수를 저장
            else:
                if gap < house:
                    house = gap
        total += house
    print(f'#{tc} {total}')

# 14
# 0 0 3 5 2 4 9 0 6 4 0 6 0 0
