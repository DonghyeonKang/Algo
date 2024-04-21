import sys 

t = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(t)]
result = []

for i in range(t):
    b1 = [1, 0]
    b2 = [0, 1]
    
    if n[i] == 0:
        result = b1
    elif n[i] == 1:
        result = b2
    else:
        for j in range(n[i] - 1):
            result = [b1[0] + b2[0], b1[1] + b2[1]]
            b1 = [b2[0], b2[1]]
            b2 = [result[0], result[1]]
    print(" ".join(list(map(str, result))))
    
