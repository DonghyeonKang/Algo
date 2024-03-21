import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
city = [sys.stdin.readline().split() for _ in range(n)]
chick = []
home = []

for i in range(n):
    for j in range(n):
        if city[i][j] =='1':
            home.append((j, i))
        elif city[i][j] == '2':
            chick.append((j, i))

result = 9999999
for chi in combinations(chick, m):
    tr = 0
    for h in home:
        tcl = 999999
        for x, y in chi:
            tcl = min(tcl, abs(h[0] - x) + abs(h[1] - y))
        tr += tcl
    result = min(result, tr)
print(result)