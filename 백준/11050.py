N, K = map(int, input().split(" "))

tmp1 = 1
tmp2 = 1
tmp3 = 1

for i in range(N):
    tmp1 = tmp1 * (N - i)

for i in range(N - K):
    tmp2 = tmp2 * (N - K - i)

for i in range(K):
    tmp3 = tmp3 * (K - i)

print(int(tmp1 / (tmp2 * tmp3)))