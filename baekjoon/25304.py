import sys

a = int(sys.stdin.readline())
n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0
for i in range(n):
    result += s[i][0] * s[i][1]

if a == result:
    print('Yes')
else:
    print('No')