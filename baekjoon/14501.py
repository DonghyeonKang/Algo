import sys

n = int(sys.stdin.readline())
t = []
p = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

g = []
for i in range(n):
    arr = []
    for j in range(n):
        if j >= i + t[i]:
            arr.append(j)
    g.append(arr)

def dfs(num):
    l = g[num]
    if len(l) == 0 and num + t[num] > n:
        return 0

    s = 0
    for i in l:
        s = max(dfs(i), s)
    return s + p[num]

result = -1
for i in range(n):
    num = dfs(i)
    result = max(num, result)
print(result)
