
# 아래와 같은 로직의 bfs 를 만든다. 
# queue 에 x, y 를 넣는다. 
# 방향 정보를 담은 리스트를 만든다. 
# queue 가 빌 때까지 아래를 반복한다. 
#   x, y 를 queue 에서 꺼낸다. 
#   반복문으로 4방향이니, 4회 아래를 반복한다. 
#      밖으로 나가면 continue
#      0 이면 continue
#      x, y == (2, 2) continue
#      x, y = (2, 2) 로 방문 처리한다. 
#      queue 에 (nx, ny) 추가한다. 
#      count += 1
# count 리턴

# 2중 for 문으로 bfs 를 반복 호출한다. 
from collections import deque

def bfs(x, y, n):
    queue = deque()
    queue.append((x, y))

    cnt = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while(queue):
        x, y = queue.popleft()
        town[x][y] = 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if town[nx][ny] == 0 or town[nx][ny] == 2:
                continue

            if town[nx][ny] == 1 and (nx, ny) not in queue:
                cnt += 1
                queue.append((nx, ny))
    return cnt


n = int(input())
town = []
for i in range(n):
    town.append(list(map(int, list(input()))))
cntSum = 0
cntPart = []

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            cntSum += 1
            cntPart.append(bfs(i, j, n))

cntPart.sort()
print(cntSum)
for i in cntPart:
    print(i)