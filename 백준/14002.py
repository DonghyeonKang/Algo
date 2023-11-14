import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]
r = []
for i in a:
    r.append([i])

for i in range(1, n):
    t = []
    for j in range(0, i):
        if a[i] > a[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                t = r[j]
    r[i] = t + r[i]

idx = dp.index(max(dp))
print(dp[idx])
print(" ".join(list(map(str, r[idx]))))