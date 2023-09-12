# 올바른 배열
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
maxCnt = 0
for i in range(n):
    firstNum = arr[i]
    cnt = 0
    for j in arr[i:]:
        if j - firstNum < 5:
            cnt += 1
        else:
            break
    if cnt > maxCnt:
        maxCnt = cnt


print(5 - maxCnt)