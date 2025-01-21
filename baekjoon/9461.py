import sys

t = int(sys.stdin.readline().strip())

a = [1, 1, 1, 2, 2]

for i in range(5, 101):
    a.append(a[i - 1] + a[i - 5])    

for i in range(t):
    n = int(sys.stdin.readline().strip())
    print(a[n - 1])