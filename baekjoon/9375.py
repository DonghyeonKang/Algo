import sys

t = int(sys.stdin.readline())
num = 0

for i in range(t):
    
    j = int(sys.stdin.readline())
    cases = {}
    
    # 데이터 저장
    for k in range(j):
        item, cate = map(str, sys.stdin.readline().strip().split(" "))
    
        if cate not in cases:
            cases[cate] = []        
    
        cases[cate].append(item)
    
    # result
    result = 1        
    for l in cases:
        result *= len(cases[l]) + 1
        
    print(result - 1)
        