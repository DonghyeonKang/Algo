import sys

n, m = map(int, sys.stdin.readline().split())
arr = ['0' for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i - 1, j):
        arr[idx] = str(k)

print(" ".join(arr))
