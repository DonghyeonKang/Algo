from collections import deque
import copy
import sys

n, m = map(int, sys.stdin.readline().split())
room = []
result = 0
for i in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))


two = deque()
for i in range(n):
    for j in range(m):
        if room[i][j] == 2:
            two.append((j, i))

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def bfs():
    global result
    queue = two.copy()
    newRoom = copy.deepcopy(room)
    
    while(queue):
        x, y = queue.popleft()
        newRoom[y][x] = 2
        for dx, dy in d:
            if x + dx >= m or y + dy >= n or x + dx < 0 or y + dy < 0 or newRoom[y + dy][x + dx] != 0:
                continue
            queue.append((x + dx, y + dy))

    cnt = 0
    for i in range(n):
        cnt += newRoom[i].count(0)
    result = max(result, cnt)


def makeWall(num):
    if num == 3:
        bfs()
        return
    for y in range(n):
        for x in range(m):
            if room[y][x] == 0:
                room[y][x] = 1
                makeWall(num + 1)
                room[y][x] = 0

makeWall(0)
print(result)