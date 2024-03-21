# 줄 세우기
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n + 1)]

for i in range(n):
    dp[a[i]] = i + 1    

m = 1
c = 1
for i in range(1, n):
    if dp[i] < dp[i + 1]:
        c += 1
    else:
        c = 1

    if m < c:
        m = c

print(n - m)