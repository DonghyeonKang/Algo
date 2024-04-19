import sys

n = int(sys.stdin.readline())

fact = 1
for i in range(1, n + 1):
    fact *= i

result = list(str(fact))
cnt = 0
for i in range(len(result) - 1, 0, -1):
    if result[i] != '0':
        break
    else:
        cnt += 1

print(cnt)