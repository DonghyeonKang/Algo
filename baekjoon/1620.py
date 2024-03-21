import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
ps = {}
psi = {}

for i in range(n):
    s = sys.stdin.readline().rstrip()
    ps[s] = i + 1
    psi[i + 1] = s

for i in range(m):
    t = sys.stdin.readline().rstrip()
    if t.isdigit():
        print(psi[int(t)])
    else:
        print(ps[t])