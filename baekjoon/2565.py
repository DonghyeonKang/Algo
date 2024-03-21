# 전깃줄
import sys

n = int(sys.stdin.readline())

a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

dp = [1 for _ in range(n)]
a.sort()

for i in range(1, n):
    for j in range(0, i):
        if a[i][1] > a[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))