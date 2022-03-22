import sys 

n, k = map(int, sys.stdin.readline().split())
v = [i for i in range(1, n + 1)]

cnt = 1
p = 0
lenV = n

print("<", end="")
while(lenV > 0):
    for i in range(k - 1):
        v.append(v[0])
        del v[0]

    if lenV == 1:
        print(v[0], end="")
    else:
        print(v[0], end=", ")

    del v[0]
    lenV -= 1
print(">", end="")