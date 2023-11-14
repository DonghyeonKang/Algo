# 1이 될 때까지
# 어떤 수 n이 1이될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행하고자 한다. 
# 단, 2번째 연산은 n이 k로 나누어 떨어질 때만 선택할 수 있다. 
# 1. n에서 1을 뺀다. 
# 2. n을 k로 나눈다. 

# n을 0일때까지 아래를 반복한다. 
# n을 k로 나눈 나머지를 구한다. 
# 1. 나머지가 0이면 
#   n을 k로 나눈 값을 n에 넣는다. 
#   count 값을 1 추가한다. 
# 2. 아니면
#   n - 나머지를 n에 넣는다.
#   count + 나머지를 count 에 넣는다. 
# count - 1 값을 출력한다. 


n, k = map(int, input().split())
count = 0

while(n > 0):
    remain = n % k
    if remain == 0:
        n //= k
        count += 1
    else:
        n -= remain
        count += remain

print(count - 1)