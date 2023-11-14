# 팰린드롬인지 확인하기

s = list(input())
a = s.copy()
s.reverse()

if s == a:
    print(1)
else:
    print(0)