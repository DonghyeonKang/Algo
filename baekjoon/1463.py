import sys 

n = int(sys.stdin.readline())
dp = [0]

for i in range(1, n + 1):
    tmp = dp[-1] + 1
    
    if i % 2 == 0:
        tmp = min(dp[i // 2] + 1, tmp)

    if i % 3 == 0:
        tmp = min(dp[i // 3] + 1, tmp)
    
    dp.append(tmp)
print(dp[n] - 1)