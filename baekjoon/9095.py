import sys

n = int(sys.stdin.readline().strip())
arr = [1, 2, 4]
for i in range(3, 10):
    arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])

for i in range(n):
    a = int(sys.stdin.readline().strip())
    print(arr[a - 1])