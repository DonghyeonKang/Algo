# 미로 탈출 
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n, m = map(int, input())
maze = []

for _ in range(n):
    maze.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 벗어난 경우는 제외
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우 제외 
            if maze[nx][ny] == 0:
                continue

            # 노드를 처음 방문하는 경우에만 최단거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))            
    return maze[n - 1][m - 1]

print(bfs(0, 0))