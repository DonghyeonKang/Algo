# 내리막길
m, n = map(int, input().split())
hillMap = []

for _ in range(m):
    hillMap.append(list(map(int, input().split())))

visited = [[-1 for _ in range(n)] for _ in range(m)]

def dfs(x, y, last):
    # 나가면 리턴
    if x < 0 or y < 0 or x >= n or y >= m:
        return 0

    # 높은 곳으로 가면 리턴    
    if hillMap[y][x] >= last:
        return 0

    # 이미 방문했었다면 그 숫자를 리턴
    if visited[y][x] > -1:
        return visited[y][x]

    # 도착시 1 리턴
    if x == (n - 1) and y == (m - 1):
        return 1

    sumResult = 0
    sumResult += dfs(x, y - 1, hillMap[y][x]) # 상
    sumResult += dfs(x, y + 1, hillMap[y][x]) # 하
    sumResult += dfs(x - 1, y, hillMap[y][x]) # 좌
    sumResult += dfs(x + 1, y, hillMap[y][x]) # 우
    visited[y][x] = sumResult
    return sumResult


result = dfs(0, 0, 10001)
print(result)