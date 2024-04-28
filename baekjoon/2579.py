import sys

n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(n)]

dp[0] = stair[0]
if n > 1:
    dp[1] = stair[0] + stair[1]
if n > 2:
    dp[2] = stair[2] + max(stair[0], stair[1])

for i in range(3, n):
    dp[i] = stair[i] + max(dp[i - 3] + stair[i - 1], dp[i - 2])
    
print(dp[-1])