import sys

n = sys.stdin.readline()
l = sys.stdin.readline().split()
s = sys.stdin.readline().strip()
result = 0
for i in l:
    if i == s:
        result += 1

print(result)