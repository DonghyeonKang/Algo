n, m = map(int, input().split())

h = list(map(int, input().split()))

h.sort()

for i in h:
    if i <= m:
        m += 1

print(m)