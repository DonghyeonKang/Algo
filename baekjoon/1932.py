import sys

n = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(i)] for i in range(1, n + 1)]

for i in range(n - 1):
    for j in range(len(dp[i])):
        if i == 0 and j == 0:
            dp[i][j] = tri[0][0]

        if dp[i + 1][j] < dp[i][j] + tri[i + 1][j]:
            dp[i + 1][j] = dp[i][j] + tri[i + 1][j]
        if dp[i + 1][j + 1] < dp[i][j] + tri[i + 1][j + 1]:
            dp[i + 1][j + 1] = dp[i][j] + tri[i + 1][j + 1]

if n == 1:
    print(tri[0][0])
else:
    print(max(dp[-1]))