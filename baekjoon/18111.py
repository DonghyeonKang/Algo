import sys

# 입력
n, m ,b = map(int, sys.stdin.readline().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 최대 최소
minn = 999
maxn = -1
for i in range(n):
    for j in range(m):
        minn = min(minn, world[i][j])
        maxn = max(maxn, world[i][j])

# 계산
height = 0
time = 999999999
for i in range(minn, maxn + 1): # 256
    arr = [0, 0]

    for j in range(n): # 500
        for k in range(m): # 500 
            tmp = world[j][k] - i

            if tmp > 0:
                arr[0] += tmp
            else:
                arr[1] += tmp
    
    if arr[1] + b + arr[0] >= 0:
        t = arr[0] * 2 + arr[1] * -1
        if t <= time:
            time = t
            height = i

print(time, height)