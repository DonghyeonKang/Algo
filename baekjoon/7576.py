# 토마토 

# bfs(x, y)
#   queue
#   queue. append(x, y)
#   dx, dy = [-1, 1, 0, 0]
#   day = 0
#   while(queue):
#      x, y = queue.popleft()
#      nx, xy
#      if 나가면 무시
#      if -1 또는 1 이면 무시
#      day += 1
#      if 0 이고 queue 에 없으면s
#          queue 에 nx, ny 넣기
#          field[nx][ny] = 1
#   return day

# day = 0
# 2중 for
#   1이면
#      day += bfs()

# flag = true
# 2 중 for
#   민약 0이 있으면
#       flag = false
# if flag:
#   print(day)
from collections import deque
import sys

def bfs():
    queue = deque()
    for x in range(n):
        for y in range(m):
             if field[x][y] == 1:
                queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if field[nx][ny] == -1 or field[nx][ny] == 1:
                continue

            if field[nx][ny] == 0:
                queue.append((nx, ny))
                field[nx][ny] = field[x][y] + 1
    return (x, y)

m, n = map(int, sys.stdin.readline().split())
field = []
for i in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

x, y = bfs()
day = field[x][y]
 

for x in range(n):
    for y in range(m):
        if field[x][y] == 0:
            day = -1
            break
if day > 0:
    day -= 1
print(day)
