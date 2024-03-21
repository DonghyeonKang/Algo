# 1로 만들기
import sys

n = int(sys.stdin.readline().rstrip())

# 3으로 나누어 떨어지면 3으로 나눈다. 
# 2로 나누어 떨어지면 2로 나눈다. 
# 1을 뺀다. 

cnt = 0
while(n > 10):
    print(n)
    if n % 3 == 0:
        cnt += 1
        n = n // 3
        continue
    if n % 2 == 0:
        cnt += 1
        n = n // 2
        continue
    cnt += 1
    n = n - 1

while(n > 3):
    print(n)
    if n % 3 == 0:
        cnt += 1
        n = n // 3
        continue
    if (n - 1) % 3 == 0:
        cnt += 2
        n = (n - 1) // 3
        continue
    if n % 2 == 0:
        cnt += 1
        n = n // 2
        continue
    cnt += 1
    n = n - 1


if n == 1:
    print(cnt)
else:
    print(cnt + 1)

# ------------------ 40일때 최소가 아님. -1 횟수가 너무 많음