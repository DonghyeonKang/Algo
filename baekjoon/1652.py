# 누울 자리를 찾아라
# n^2 을 2회 탐색하는 방식

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(input()))

garo = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][j] == '.':
            cnt += 1
        
        if arr[i][j] == 'X':
            if cnt >= 2:
                garo += 1
            cnt = 0
    if cnt >= 2:
        garo += 1

sero = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[j][i] == '.':
            cnt += 1        

        if arr[j][i] == 'X':
            if cnt >= 2:
                sero += 1
            cnt = 0
    if cnt >= 2:
        sero += 1

print(garo, sero)