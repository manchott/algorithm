import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
d = defaultdict(int)
for i in range(N):
    d[int(input())] += 1

max_value = max(d.values())

for k, v in sorted(d.items()):
    if v == max_value:
        print(k)
        exit()