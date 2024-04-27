import sys

n, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(v)
mid = (start + end) // 2

while(start < end):
    if mid == start:
        break
    
    sumTree = 0
    for i in v:
        remain = i - mid
        if remain > 0:
            sumTree += remain
    
    if sumTree == m:
        break
    
    if sumTree > m:
        start = mid
    else:
        end = mid
    mid = (start + end) // 2


print(mid)