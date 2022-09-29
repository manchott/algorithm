import sys
input = sys.stdin.readline

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x > y:
            Vroot[x] = y
        else:
            Vroot[y] = x

def calc_distance(x, y):  
    x1, y1, x2, y2 = x[0], x[1], y[0], y[1]
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance

N, M = map(int, input().split())
Vroot = [i for i in range(N+1)]
nodes = [0] + [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)
Elist = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        w = calc_distance(nodes[i], nodes[j])
        Elist.append([i, j, w])
Elist.sort(key=lambda x: x[2])
answer = 0
for s, e, w in Elist:
    if find(s) != find(e):
        union(s, e)
        answer += w
 
print("{:.2f}".format(answer))