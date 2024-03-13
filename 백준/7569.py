import sys
from collections import deque

nx, ny, nz = map(int, sys.stdin.readline().split())

box = [[sys.stdin.readline().split() for _ in range(ny)] for _ in range(nz)]
d = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]

red = deque()
green = 0
for i in range(nz):
    for j in range(ny):
        for k in range(nx):
            if box[i][j][k] == '1':
                red.append((k, j, i))
            elif box[i][j][k] == '0':
                green += 1
                
def bfs(box, red):
    global green
    queue = red
    cnt = 0
    addQueue = deque()
    while(queue or addQueue):
        addQueue = deque()
        
        while(queue):
            x, y, z = queue.popleft()
            for dx, dy, dz in d:
                if x + dx < 0 or y + dy < 0 or z + dz < 0 or x + dx >= nx or y + dy >= ny or z + dz >= nz or box[z + dz][y + dy][x + dx] == '-1' or box[z + dz][y + dy][x + dx] == '1': # 벗어남 or 빈칸
                    continue
                box[z + dz][y + dy][x + dx] = '1'
                green -= 1
                addQueue.append((x + dx, y + dy, z + dz))
        cnt += 1      
        queue = addQueue.copy()      
    return cnt

if green == 0: # 모두 익어있는 상태
    print(0)
else:
    result = bfs(box, red)
    if green > 0:
        print(-1)
    else:
        print(result - 1)