import sys

n, m = map(int, sys.stdin.readline().split())
ms = []
stack = {}
result = 0

for _ in range(m):
   ms.append(sys.stdin.readline().split())

ms.sort(key=lambda x:x[2])

for i in ms:
    flag = False
    if not stack.get(i[0]):
        stack[i[0]] = 1
        flag = True
    if not stack.get(i[1]):
        stack[i[1]] = 1
        flag = True
    if flag:
        result += int(i[2])
        print(result)

print(stack)
print(result)

# 3% 시간초과 ---------
# for _ in range(m):
#    ms.append(list(map(int, input().split())))

# ms.sort(key=lambda x:x[2])

# for i in ms:
#     flag = False
#     if i[0] not in stack:
#         stack.append(i[0])
#         flag = True
#     if i[1] not in stack:
#         stack.append(i[1])
#         flag = True
#     if flag:
#         result += i[2]

# print(result)

# 1% 시간초과 ---------
# while(len(stack) < n):
#     minN = ms[0][2]
#     minI = 0
#     for i, data in enumerate(ms):
#         if data[2] < minN:
#             minN = data[2]
#             minI = i
    
#     if len(stack) == 0:
#         stack.append(ms[minI][0])
#         stack.append(ms[minI][1])
#         result.append(ms[minI][2])
#     elif ms[minI][1] not in stack:
#         stack.append(ms[minI][1])
#         result.append(ms[minI][2])
#     del ms[minI]

# print(sum(result))
    