M, N = map(int, input().split())
S = int(input())
stores = []
for i in range(S):
    x, y = map(int, input().split())
    stores.append([x, y])
dx, dy  = map(int, input().split())
for store in stores:
    # 만약 상점과 동근이가 마주보고 있다면
    if store[0] * dx == 2:
        
    elif store[0] * dx == 12:

