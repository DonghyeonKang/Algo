import sys
sys.setrecursionlimit(1000)

n, m = map(int, sys.stdin.readline().split())
y, x, direction = map(int, sys.stdin.readline().split())
home = [sys.stdin.readline().split() for _ in range(n)]
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
result = 0

while(True):
    # 청소
    if home[y][x] == '0':
        home[y][x] = '2'
        result += 1

    # 4방향 모두 청소 됨 or 벽
    if (home[y + 1][x] == '1' or home[y + 1][x] == '2') and (home[y - 1][x] == '1' or home[y - 1][x] == '2') and (home[y][x + 1] == '1' or home[y][x + 1] == '2') and (home[y][x - 1] == '1' or home[y][x - 1] == '2'):
        antid = direction + 2
        if antid >= 4:
            antid -= 4

        # 종료 조건, 뒷 방향이 벽이면 종료
        dx, dy = d[antid]
        if home[y + dy][x + dx] == '1':
            break
        x += dx
        y += dy
        continue

    # 회전
    direction -= 1
    if direction < 0:
        direction = 3

    # 이동
    dx, dy = d[direction]
    if home[y + dy][x + dx] == '0':
        x += dx
        y += dy

print(result)
