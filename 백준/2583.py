import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)

n, m, k = map(int, input().split())

box = []
paper = [[0 for _ in range(m)] for _ in range(n)]

for i in range(k):
    box.append(list(map(int, input().split())))

for i in box:
    lb = [i[0], i[1]]
    rt = [i[2], i[3]]
    for j in range(rt[1]):
        for k in range(rt[0]):
            if j >= lb[1] and k >= lb[0]:
                paper[j][k] = 1

def dfs(x, y):
    if x >= m or x < 0 or y >= n or y < 0 or paper[y][x] == 1:
        return 0
    num = 1
    paper[y][x] = 1
    num += dfs(x + 1, y)
    num += dfs(x - 1, y)
    num += dfs(x, y + 1)
    num += dfs(x, y - 1)
    return num    

tSize = []
for y in range(n):
    for x in range(m):
        s = dfs(x, y)
        if s > 0:
            tSize.append(s)

tSize.sort()
print(len(tSize))
print(*tSize)