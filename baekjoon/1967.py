import sys

n = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]

pnode = [i[0] for i in l]
cnode = [i[1] for i in l]
tnode = []

for i in cnode: # 단말 노드
    if i not in pnode:
        tnode.append(i)

def dfs(snode, enode, weight):
    if enode in tnode and visited[snode - 1] == 1:
        return weight

    visited[snode - 1] = 1
    visited[enode - 1] = 1
    nodes = []

    for i in l: # 연결된 노드 모두 넣기
        # 부모 노드와 연결된 자식 노드 추가
        if i[0] == snode and visited[i[1] - 1] == 0:
            nodes.append(i)
            visited[i[1] - 1] = 1
        # 부모 노드와 연결된 부모 노드 추가
        if i[1] == snode and visited[i[0] - 1] == 0:
            nodes.append(i)
            visited[i[0] - 1] = 1
         
        # 자식 노드와 연결된 부모 노드 추가
        if i[0] == enode and visited[i[1] - 1] == 0:
            nodes.append(i)
            visited[i[1] - 1] = 1

    s = 0
    for i in nodes:
        s = max(dfs(i[0], i[1], i[2]), s)
    return s + weight

result = 0
node = []
for i in l: # 가장 끝 노드
    if i[1] in tnode:
        node.append(i)

for i in node:
    visited = [0 for _ in range(n)]
    result = max(dfs(i[0], i[1], i[2]), result)
print(result)