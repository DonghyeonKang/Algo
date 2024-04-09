import sys
import heapq

n, vsize = map(int, sys.stdin.readline().split())
v = [[] for _ in range(n)]
tmp = [[] for _ in range(n)]

for i in range(vsize):
    s, e = map(int, sys.stdin.readline().split())
    tmp[e - 1].append(s)
    v[s - 1].append(e)


nodes = [len(tmp[i]) for i in range(n)] # 노드의 차수
heap = []

# 시작 노드 넣기
for i in range(len(nodes)):
    if nodes[i] == 0:
        heapq.heappush(heap, i + 1)
result = []

while(heap):
    # 노드를 지움
    node = heapq.heappop(heap)
    result.append(str(node))

    # 노드와 연결된 다른 노드의 차수 1감소 만약 차수가 0이 되면 queue 에 넣기
    for i in v[node - 1]:
        nodes[i - 1] -= 1
        if nodes[i - 1] == 0:
            heapq.heappush(heap, i)

if n == 1:
    print(1)
else:
    print(" ".join(result))