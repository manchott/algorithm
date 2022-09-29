import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
distance = [float('inf')] * (V + 1)
distance[K] = 0

grid = defaultdict(list)
for _ in range(E):
    s, e, w = map(int, input().split())
    grid[s].append((e, w))

heap = []
heapq.heappush(heap, (0, K))
while heap:
    w, n = heapq.heappop(heap)
    if distance[n] < w:
        continue
    for e, dist in grid[n]:
        if distance[e] > w + dist:
            distance[e] = w + dist
            heapq.heappush(heap, (w + dist, e))

for i in range(1, V + 1):
    print(distance[i] if distance[i] != float('inf') else "INF")
