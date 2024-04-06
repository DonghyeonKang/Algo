import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
idx = -1

# 가장 큰 동전 찾기
for i in range(n - 1, -1, -1):
    if coins[i] <= k:
        idx = i
        break

result = 0
for i in range(idx, -1, -1):
    result += k // coins[i]
    k = k % coins[i]
    if k == 0:
        break

print(result)