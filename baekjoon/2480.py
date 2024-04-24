a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a != b and b != c and c != a:
    tmp = max(a, -1)
    tmp = max(b, tmp)
    tmp = max(c, tmp)
    print(tmp * 100)
else:
    if a == b:
        print(1000 + a * 100)
    elif a == c:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
