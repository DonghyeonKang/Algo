# 줄세우기

import sys

n = int(sys.stdin.readline())
a = []

for _ in range(n):
    a.append(int(sys.stdin.readline()))

dp = [1]
for i in range(1, n):
    dp.append(1)
    for j in range(0, i):
        if a[i] > a[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    
print(n - max(dp))