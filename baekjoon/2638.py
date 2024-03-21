# 치즈 

import sys
sys.setrecursionlimit(15000)

# 입력
n, m = map(int, input().split())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))
hours = 0 # 치즈가 다 녹을 때 까지 시간
visited = [[0 for _ in range(m)] for _ in range(n)]
melting = [] 

# dfs 로 공기 분리 
def dfsOutsideAir(x, y):
    if x < 0 or y < 0 or y >= n or x >= m:
        return

    if paper[y][x] == 1 or paper[y][x] == 3:
        return
    
    paper[y][x] = 3

    dfsOutsideAir(x, y - 1) # 상 
    dfsOutsideAir(x, y + 1) # 하
    dfsOutsideAir(x - 1, y) # 좌
    dfsOutsideAir(x + 1, y) # 우    
    return

def toOutside(x, y):
    if x < 0 or y < 0 or y >= n or x >= m:
        return

    if visited[y][x] == 1:
        return 0

    if paper[y][x] == 1:
        return
    
    if paper[y][x] == 0:
        paper[y][x] = 3
    visited[y][x] = 1
    toOutside(x, y - 1) # 상 
    toOutside(x, y + 1) # 하
    toOutside(x - 1, y) # 좌
    toOutside(x + 1, y) # 우    
    return

# 치즈 탐색 dfs
def dfs(x, y):
    if x < 0 or y < 0 or y >= n or x >= m:
        return 0

    if visited[y][x] == 1:
        return 0

    if paper[y][x] == 0:
        return 0
    
    if paper[y][x] == 3:
        return 1 

    # 방문 처리
    visited[y][x] = 1
    sumAir = 0
    sumAir += dfs(x, y - 1) # 상 
    sumAir += dfs(x, y + 1) # 하
    sumAir += dfs(x - 1, y) # 좌
    sumAir += dfs(x + 1, y) # 우    

    # 치즈 녹음
    if sumAir >= 2: 
        melting.append((x, y))
    return 0

# ---------------------------- main ---------------
# 바깥 공기 분리
dfsOutsideAir(0, 0)

# 치즈 녹이기
while(True):
    # 녹일 부분 찾기
    for i in range(m):
        for j in range(n):
            dfs(i, j)

    # 녹일 부분 없으면 종료
    if len(melting) == 0:
        break

    # 녹이기
    for i in melting:
        paper[i[1]][i[0]] = 3
    melting = []
    # 시간 추가
    hours += 1
    # 방문 정보 초기화
    visited = [[0 for _ in range(m)] for _ in range(n)]
    toOutside(0, 0)
    visited = [[0 for _ in range(m)] for _ in range(n)]
print(hours)