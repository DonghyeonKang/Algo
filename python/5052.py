# 전화번호 목록
import sys

test = int(sys.stdin.readline().rstrip())
n = []
nums = []

# 입력
for i in range(test):
    n.append(int(sys.stdin.readline().rstrip()))
    nums.append([])
    for j in range(n[i]):
        nums[i].append(sys.stdin.readline().rstrip())

# 결과
result = []
for i in nums:
    flag = True
    for j in range(len(i)):
        remain = i.copy()
        del remain[j]

        for k in remain:
            if len(k) >= len(i[j]) and i[j] == k[:len(i[j])]:
                flag = False
    
    if flag:
        result.append('YES')
    else:
        result.append('NO')

# 결과
result = []
for i in nums:
    flag = True
    for j in range(len(i)):
        a = i[j]
        for k in i[j + 1:]:
            if str(a) == str(k)[:len(str(a))]:
                flag = False
    
    if flag:
        result.append('YES')
    else:
        result.append('NO')

print("\n".join(result))


# # 전화번호 목록

# test = int(input())
# n = []
# nums = []

# # 입력
# for i in range(test):
#     n.append(int(input()))
#     nums.append([])
#     for j in range(n[i]):
#         nums[i].append(int(input()))

# # 정렬
# for i in nums:
#     i.sort()

# # 결과
# result = []
# for i in nums:
#     flag = True
#     for j in range(len(i)):
#         a = i[j]
#         for k in i[j + 1:]:
#             if str(a) == str(k)[:len(str(a))]:
#                 flag = False
    
#     if flag:
#         result.append('YES')
#     else:
#         result.append('NO')

# for i in result:
#     print(i)