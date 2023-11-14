# 유기농 배추

# 값을 입력 받는다. 
# dfs(x, y)
#   범위 벗어나면
#       return
#   x, y 을 방문 처리한다. 
#   n이 0이면
#       return false
#   아니면
#   dfs() 상
#   dfs() 하
#   dfs() 좌
#   dfs() 우
#   return true
#   배추 밭의 넓이만큼 아래를 반복
#           dfs(x, y)

import sys
sys.setrecursionlimit(10000)

# 변수
testCase = int(input())
field = []
visited = []
nList = []
mList = []

for i in range(testCase):
    m, n, k = map(int, input().split())
    nList.append(n)
    mList.append(m)
    field.append([[0 for _ in range(m)] for _ in range(n)])
    visited.append([[0 for _ in range(m)] for _ in range(n)])
    for j in range(k):
        x, y = map(int, input().split())
        field[i][y][x] = 1

def dfs(x, y, i):
    # 벗어남 처리
    if x < 0 or y < 0 or x >= mList[i] or y >= nList[i]:
        return

    # 방문 처리, 방문했었으면 리턴
    if visited[i][y][x] == 1:
        return
    else:
        visited[i][y][x] = 1    

    # 0 이면 리턴 당함
    if field[i][y][x] == 0:
        return

    # dfs 호출
    dfs(x, y - 1, i) # 상 
    dfs(x, y + 1, i) # 하
    dfs(x - 1, y, i) # 좌
    dfs(x + 1, y, i) # 우 
    return True

result = []
for i in range(len(field)):
    result.append(0)
    for y in range(len(field[i])):
        for x in range(len(field[i][y])):
            if dfs(x, y, i):
                result[i] += 1
for i in result:
    print(i)