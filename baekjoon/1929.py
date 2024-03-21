# import math
# n, m = map(int, input().split())

# for i in range(n, m + 1):
#     flag = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             flag = False
#     if flag:
#         print(i)

import math
n, m = map(int, input().split())

def isPrime(i):
    if i == 1:
        return False
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True

for i in range(n, m + 1):
    if isPrime(i):
        print(i)
