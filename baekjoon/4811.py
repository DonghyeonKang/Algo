n = 30
b = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    b[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            b[i][j] = b[i - 1][j] + b[i][j - 1]

while(1):
    a = int(input())
    if a == 0:
        break
    print(b[a][a])
    