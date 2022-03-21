import sys 

n, k = map(int, sys.stdin.readline().split())
v = [i for i in range(1, n + 1)]

cnt = 1
p = 0
lenV = n

print("<", end="")
while(lenV > 0):
    if cnt == k:
        if lenV == 1:
            print(v[p], end="")
        else:
            print(v[p], end=", ")
        del v[p]
        cnt = 1
        lenV -= 1

    if lenV - 1 == p:
        p = 0
        cnt += 1
    elif lenV - 1 < p:
        p = 0
        cnt = 1
    else:
        cnt += 1
        p += 1
print(">", end="")