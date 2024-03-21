# 문자열 집합

n, m = map(int, input().split())

s = []
strings = []
for i in range(n):
    s.append(input())
for i in range(m):
    strings.append(input())

cnt = 0
for i in strings:
    if i in s:
        cnt += 1
print(cnt)