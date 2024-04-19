h, m = map(int, input().split())
t = int(input())

mt = m + t
if mt >= 60:
    h += (mt // 60)
    mt = mt % 60

if h >= 24:
    h = h - 24

print(h, mt)