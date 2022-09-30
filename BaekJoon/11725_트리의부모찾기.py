import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    visited[1] = 0
    Q = deque()
    Q.append(1)
    while Q:
        x = Q.popleft()
        for node in nodes[x]:
            if not visited[node]:
                visited[node] = 1
                parent[node] = x
                Q.append(node)


N = int(input())
nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
visited = [0] * (N + 1)
parent = [0] * (N + 1)
BFS()
for i in range(2, N + 1):
    print(parent[i])
