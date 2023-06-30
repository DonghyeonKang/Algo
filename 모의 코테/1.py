# 좀비 떼가 기관총 진지에도 오다니
import sys

def result(zombies, ml, mk, c):
    sum = mk

    for i in zombies:

        if i > sum: # 크레모아를 써야함
            if(c == 0):
                return "NO"
            c -= 1
            sum -= mk # 크레모아를 터뜨리면 기관총을 쏘지 못함
        
        if(sum < ml * mk): # sum 누적
            sum += mk

    return "YES"

l = int(sys.stdin.readline())
ml,mk=map(int, sys.stdin.readline().split())
c =int(sys.stdin.readline())
zombies= []

for i in range(l):
    zombies.append(int(sys.stdin.readline()))

print(result(zombies, ml, mk, c))