A, B, V = map(int, input().split(" "))

day = 1 + int((V - A) / (A - B))
if (V - A) % (A - B) > 0:
    day += 1
print(day)