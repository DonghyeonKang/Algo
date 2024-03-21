# 입력
f = list(input())
s = list(input())
dp = [[0 for _ in range(len(f) + 1)] for _ in range(len(s) + 1)]

# 값 채우기
for i in range(1, len(s) + 1):
    for j in range(1, len(f) + 1):
        if s[i - 1] == f[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len(s)][len(f)])