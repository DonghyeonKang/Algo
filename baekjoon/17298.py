import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = ['-1' for _ in range(n)]
stk = [(arr[0], 0)]

if n != 1:    
    for i in range(1, n):
        for j in range(len(stk)):
            num, idx = stk[-1]
            if num < arr[i]:
                result[idx] = str(arr[i])
                stk.pop()
            else:
                break
            
        stk.append((arr[i], i))

print(" ".join(result))