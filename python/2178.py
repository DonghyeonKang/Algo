# 미로 탐색
from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, list(input()))))

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = []

def bfs(x, y):    
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 4방향 탐색, 1이면 maze[y][x] 값 + 1 저장, bfs 호츨
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 0이면 리턴
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

bfs(0, 0)
print(maze[n - 1][m - 1])