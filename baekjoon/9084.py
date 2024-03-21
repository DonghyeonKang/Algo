
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    c = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    money = int(sys.stdin.readline())

    t = 0
    if money % coin[0] == 0:
        t = 1

    for i in range(1, c):
        for j in range(0, i):
            tmp = money // coin[j]
            cnt = 0
            while(tmp >= 0):
                tmp -= 1
                cnt += 1
                if (coin[j] * tmp) + (coin[i] * cnt) == money:
                    t += 1
    
            