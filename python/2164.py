n = int(input())
v = [i for i in range(1, n + 1)]

while(n != 1):
    if n % 2 == 1:
        limit = (n + 1) // 2
    else:
        limit = n // 2

    for i in range(0, limit):
        del v[i]
        n -= 1

print(v[0])


# import collections
# a = int(input())
# n = collections.deque([i for i in range(1, a+1)])

# while len(n) > 1:
#     n.popleft()  # 왼쪽 요소를 제거해라
#     n.rotate(-1) # 왼쪽으로 한바퀴 돌려라

# print(n[0])