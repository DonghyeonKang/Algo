import sys
import heapq

# 
n = int(sys.stdin.readline())
v = {}
degree = {}
for i in range(n):
    s, e = sys.stdin.readline().split()
    # 간선
    if s in v:
        tmp = v[s]
        heapq.heappush(tmp, e)
        v[s] = tmp
    else:
        v[s] = [e]

    # 차수
    if s not in degree:
        degree[s] = 0

    if e in degree:
        degree[e] += 1
    else:
        degree[e] = 1

# 0 차수
heap = []
keys = list(degree.keys())
for i in keys:
    if degree[i] == 0:
        heapq.heappush(heap, i)

result = []
flag = False

while(heap):
    # queue 비우기
    queue = []
    while(heap):
        node = heapq.heappop(heap)
        result.append(node)
        queue.append(node)

    for node in queue:
        if node not in v:
            continue

        toNodes = v[node]
        for _ in range(len(toNodes)):
            toNode = heapq.heappop(toNodes)

            if degree[toNode] == 0:
                flag = True
                break

            degree[toNode] -= 1
            if degree[toNode] == 0:
                heapq.heappush(heap, toNode)

if flag or len(result) != len(degree.keys()):
    print(-1)
else:
    for i in result:
        print(i)
