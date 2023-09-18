# ATM

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()
r = 0
for i in range(n):
    r = r + sum(a[:i + 1])
print(r)