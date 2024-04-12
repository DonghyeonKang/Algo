import sys 
import heapq

n, m = map(int, sys.stdin.readline().split())
heap = []
v = [[] for _ in range(n)]
d = [0 for _ in range(n)]

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    v[s - 1].append(e)
    d[e - 1] += 1

for i in range(n):
    if d[i] == 0:
        heapq.heappush(heap, i + 1)

result = []
while(heap):
    node = heapq.heappop(heap)
    result.append(str(node))
    to = v[node - 1]
    for i in range(len(to)):
        d[to[i] - 1] -= 1
        if d[to[i] - 1] == 0:
            heapq.heappush(heap, to[i])

print(" ".join(result))