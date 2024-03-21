# 게리멘더링
# 입력 받는다. 
# 구역 나누기
# 나뉜 구역에서 dfs 로 접근하지 못하면 없애기 
# 나뉜 구역별로 인구수 차이 구해서 가장 작은값 출력

from itertools import combinations
import sys

# 입력
n = int(input())
person = list(map(int, input().split()))
node = [0]
for _ in range(n):
    tmp = list(map(int, input().split()))
    node.append(tmp[1:])

# 구역 나누기
arr = [i for i in range(1, n + 1)]
nCrList = []
for i in range(1, n // 2 + 1):
    nCrList.append(combinations(arr, i))

# 나뉜 구역에서 dfs 
def dfs(start, nCr, visited):
    connected = node[start]  # start node 와 연결되어있는 노드 리스트

    # 이미 방문한 노드면 리턴
    if start in visited:
        return

    if start not in nCr:
        return

    # 방문 처리
    visited.append(start)

    # 연결된 노드 탐색
    for i in connected:
        dfs(i, nCr, visited)

# --------
acceptedCombi = []
region = [i for i in range(n + 1)]

for i in nCrList:
    for j in i:
        # 구역 나누기
        first = list(j)
        second = region.copy()[1:]
        for k in first:
            second.remove(k)
        
        # 1구역
        visited = []
        dfs(first[0], first, visited) # dfs 로 방문 노드 업데이트
        if sorted(visited) != sorted(first): # 방문한 노드와 구역1과 같으면
            continue
        
        # 2구역
        visited = []
        dfs(second[0], second, visited) # dfs 로 방문 노드 업데이트
        if sorted(visited) != sorted(second): # 방문한 노드와 구역2가 같으면
            continue

        acceptedCombi.append((first, second))

minSum = sys.maxsize

if len(acceptedCombi) > 0:
    for i in acceptedCombi:
        # 1구역 사람 수 구하기
        sumFirst = 0
        first = i[0]
        for j in first:
            sumFirst += person[j - 1]

        # 2구역 사람 수 구하기
        sumSecond = 0
        second = i[1]
        for j in second:
            sumSecond += person[j - 1]

        # 사람 수 차이 최솟값 없데이트
        sumCase = sumFirst - sumSecond
        if sumCase < 0:
            if (sumCase * -1) < minSum:
                minSum = sumCase * -1
        else:
            if sumCase < minSum:
                minSum = sumCase
    print(minSum)
else:
    print(-1)