import sys

n, m = map(int, sys.stdin.readline().split())
d = {}
for i in range(n):
    key, value = sys.stdin.readline().split()
    d[key] = value

for i in range(m):
    find = sys.stdin.readline().strip()
    print(d[find])