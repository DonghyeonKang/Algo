import sys

l = int(sys.stdin.readline())
ml, mk = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
z = [0] + [int(sys.stdin.readline()) for _ in range(l)]
s = [0]

flag = True
for i in range(1, l + 1):
    p = max(0, i - ml)
    damage = s[i - 1] - s[p] 

    if z[i] <= damage + mk:
        s.append(s[i - 1] + mk)
    else:
        if c > 0 :
            c -= 1
            s.append(s[i - 1])
        else:
            flag = False
            break

if flag:
    print("YES")
else:
    print("NO")