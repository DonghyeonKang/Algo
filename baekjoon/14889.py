import sys 
from itertools import combinations

n = int(sys.stdin.readline())
sl = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
p = [i for i in range(0, n)]

result = 99999999
l = list(combinations(p, n // 2))
for i in range(len(l) // 2):
    tmp1 = list(combinations(l[i], 2))
    skill1 = 0 
    for j in tmp1:
        skill1 += sl[j[0]][j[1]] + sl[j[1]][j[0]]
    
    tmp2 = list(combinations(l[-(i + 1)], 2))
    skill2 = 0 
    for j in tmp2:
        skill2 += sl[j[0]][j[1]] + sl[j[1]][j[0]]

    result = min(result, abs(skill1 - skill2))

print(result)
    
