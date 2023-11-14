# 반도체 설

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [a[0]]
l = 0

def bs(arr, num):
    start = 0
    end = len(arr) - 1
    
    while(start < end):
        mid = (start + end) // 2
        if arr[mid] < num:
            if start == mid:
                break
            start = mid
        else:
            end = mid

    return end

for i in range(1, n):
    if dp[l] < a[i]:
        dp.append(a[i])
        l += 1
    else:
        idx = bs(dp, a[i])
        dp[idx] = a[i]

print(len(dp))