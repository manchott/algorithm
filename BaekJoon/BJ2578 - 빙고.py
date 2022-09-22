def check(x, y):
    global bingo_num
    if not sum(bingo[x]):
        bingo_num += 1
    if not sum(list(zip(*bingo))[y]):
        bingo_num += 1
    # 오른쪽 아래로 가는 대각선 체크
    if x == y:
        if not sum(bingo[i][i] for i in range(5)):
            bingo_num += 1
    # 왼쪽 아래로 가는 대각선 체크
    if x + y == 4:
        if not sum(bingo[i][4 - i] for i in range(5)):
            bingo_num += 1
        


answer = bingo_num = 0
bingo = [list(map(int, input().split())) for _ in range(5)]
idx_bingo = []
for i in range(5):
    idx_bingo += bingo[i]
announce = []
for _ in range(5):
    announce += list(map(int, input().split()))
for i in range(25):
    if announce[i] in idx_bingo:
        idx = idx_bingo.index(announce[i])
        x, y = idx // 5, idx % 5
        bingo[x][y] = 0
        check(x, y)
        if bingo_num >= 3:
            answer = i
            break
print(answer + 1)
