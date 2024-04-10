import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
v = [[] for _ in range(n)]
depth = [1 for _ in range(n)]

# 간선
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    v[s - 1].append(e)
    
# depth 측정
queue = deque()
for i in range(n):
    nodes = v[i]

    if len(nodes) == 0:
        continue

    for j in nodes:
        queue.append(j)
    
    while(queue):
        node = queue.popleft()
        
        if depth[node - 1] <= depth[i]:
            depth[node - 1] = depth[i] + 1

depth = map(str, depth)
print(" ".join(depth))