import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
flag = True
result = 0

while(1):
    flag = True
    visit = [[0 for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if visit[y][x] == 1:
                continue

            queue.append((x, y))
            idx = [(x, y)]
            visit[y][x] = 1
            sum = 0

            while(queue):
                # 연합에 추가
                x, y = queue.popleft()
                sum += world[y][x]

                for dx, dy in d:
                    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n or visit[y + dy][x + dx] == 1:
                        continue

                    # 방문, 큐 업데이트
                    if l <= abs(world[y][x] - world[y + dy][x + dx]) <= r:
                        queue.append((x + dx, y + dy))
                        visit[dy + y][dx + x] = 1
                        idx.append((x + dx, y + dy))
                        flag = False

            # 인구 업데이트
            update = sum // len(idx)
            for x, y in idx:
                world[y][x] = update
    if flag:
        break
    result += 1

print(result)