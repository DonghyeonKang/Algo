# 얼음 얼려먹기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위 벗어남
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상 
        dfs(x, y - 1)
        # 하
        dfs(x, y + 1)
        # 좌
        dfs(x - 1, y)
        # 우 
        dfs(x + 1, y)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)