# 피보나치 수 2

n = int(input())

last = 0
fibo = 1
for i in range(n - 1):
    tmp = fibo
    fibo = last + fibo
    last = tmp
    
print(fibo)
