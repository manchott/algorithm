# 1238_Contact
# 22-09-14

from collections import deque
import sys
sys.stdin = open('input.txt','rt')

T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    L = list(map(int, input().split()))
    edges = [[] for _ in range(101)]
    visited = [0] * 101
    queue = deque()

    for i in range(0, N, 2):
        edges[L[i]].append(L[i + 1])
    # BFS
    visited[S] += 1
    for edge in edges[S]:
        queue.append((S, edge))
    while queue:
        s, e = queue.popleft()
        if not visited[e]:
            visited[e] = visited[s] + 1
            for edge in edges[e]:
                queue.append((e, edge))

    max_visit, max_idx = 0, S
    for i in range(101):
        if max_visit <= visited[i]:
            max_visit, max_idx = visited[i], i
    print('#{} {}'.format(tc, max_idx))

