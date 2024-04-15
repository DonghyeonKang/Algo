import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sorted(list(map(int, sys.stdin.readline().split())))

diff = []
tmp = s[0]
for i in range(1, n):
    diff.append(abs(tmp - s[i]))
    tmp = s[i]

arr = sorted(diff)
arr = arr[:len(arr) - m + 1]
print(sum(arr))


