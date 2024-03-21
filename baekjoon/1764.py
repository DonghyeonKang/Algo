import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = []
b = {}

for i in range(n):
    a.append(sys.stdin.readline().strip())

for i in range(m):
    tmp = sys.stdin.readline().strip()
    b[tmp] = tmp

ab = []
for i in range(n):
    if b.get(a[i]):
        ab.append(b[a[i]])

ab.sort()
print(len(ab))
for i in ab:
    print(i)