import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

result = 0
for i in a:
    result += i // t
    if(i % t > 0):
        result += 1

print(result)
print(n // p, n % p)