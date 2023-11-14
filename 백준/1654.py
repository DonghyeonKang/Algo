import sys

k, n = map(int, input().split())
v = []

max = 0
min = 1

for i in range(k):
    tmp = int(sys.stdin.readline())
    if tmp > max:
        max = tmp
    v.append(tmp)

max += 1

while(min < max):
    sum = 0
    mid = min + ((max - min) // 2)
    for i in range(len(v)):
        sum += v[i] // mid

    if sum == n:
        tmpResult = mid
    elif sum < n:
        max = mid
    else:
        min = mid + 1

if sum < n:
    print(tmpResult)
else:
    print(mid)