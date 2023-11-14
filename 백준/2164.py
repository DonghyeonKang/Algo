# n = int(input())
# v = [i for i in range(1, n + 1)]

# while(n != 1):
#     if n % 2 == 1:
#         limit = (n + 1) // 2
#     else:
#         limit = n // 2

#     for i in range(0, limit):
#         del v[i]
#         n -= 1

# print(v[0])


import collections
a = int(input())
v = collections.deque([i for i in range(1, a+1)])

while len(v) > 1:
    v.popleft()  
    v.rotate(-1)

print(v[0])