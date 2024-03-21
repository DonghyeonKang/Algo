# 입력 
n, k = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]
coins.sort()

# dp 배열 생성
dp = [10001] * (k + 1)
dp[0] = 0

for i in range(1, k + 1):
    for coin in coins:
        if i - coin < 0:
            break
        else:
            dp[i] = min(dp[i - coin] + 1, dp[i])

if dp[k] == 10001:
    print("-1")
else:
    print(dp[k])