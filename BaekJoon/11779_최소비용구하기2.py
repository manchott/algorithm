import heapq, sys
input = sys.stdin.readline

N = int(input())
M = int(input())
grid = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    grid[s].append((e, w))
S, E = map(int, input().split())
nearest = [S] * (N + 1)
distance = [float('inf')] * (N + 1)
distance[S] = 0

heap = []
heapq.heappush(heap, (0, S))
while heap:
    w, n = heapq.heappop(heap)
    if distance[n] < w:
        continue
    for e, nw in grid[n]:
        d = w + nw
        if d < distance[e]:
            distance[e], nearest[e] = d, n
            heapq.heappush(heap, (d, e))

result = []
temp = E
while temp != S:
    result.append(temp)
    temp = nearest[temp]
result.append(S)
result.reverse()

print(distance[E])
print(len(result))
print(*result)
