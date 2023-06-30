# 숫자 고르기

# 입력 받음
# 1번 노드부터 n 번 노드까지 아래를 반복
#   i 번 노드와 노드와 연결된 노드 스택에 저장
#   스택 사이즈가 0이 될 때까지 아래를 반복
#       스택 상단에 있는 노드가 스택의 다른 위치에 존재한다면
#           사이클 리스트에 노드 추가
#       tmp 리스트에 스택에서 pop한 값을 넣는다. 
#       pop 한 노드와 연결된 노드가 사이클 리스트에 없다면
#            스택에 추가
# 사이클 길이 출력
# 사이클 원소 정렬 후 하나씩 출력


n = int(input())
nums = {}
for i in range(1, n + 1):
    nums[i] = int(input())

visited = [0 for _ in range(n + 1)]
result = []

def dfs(n):
    if visited[n] == 1:
        return n
    
    visited[n] = 1
    m = dfs(nums[n])

    if m not in result and m != None:
        result.append(m)
        
for i in range(1, len(nums) + 1):
    visited = [0 for _ in range(n + 1)]
    dfs(nums[i])


result.sort()
print(len(result))
for i in result:
    print(i)










# n = int(input())
# nums = {}
# for i in range(1, n + 1):
#     nums[i] = int(input())

# stk = []
# cycle = []
# for i in range(1, n + 1):
#     stk.append(i)
#     stk.append(nums[i])
#     tmp = []
#     while (len(stk) > 0):
#         # 스택 상단에 있는 노드가 스택에 이미 존재한다면 tmp를 사이클에 추가
#         if stk[-1] in stk[:len(stk) - 1]:
#             tmp.append(stk[-1])
#             stk = []
#             for j in tmp:
#                 if nums[num] not in cycle:
#                     cycle.append(j)
#             continue

#         # tmp 리스트에 스택에서 pop 한 값 넣음
#         num = stk.pop()
#         tmp.append(num)

#         # pop 한 노드가 사이클에 없다면 pop한 노드와 연결된 노드 스택에 추가
#         if num not in cycle:
#             stk.append(nums[num])
#             if nums[num] == tmp[-1] and nums[num] not in cycle:
#                 cycle.append(nums[num])

# cycle.sort()
# for i in cycle:
#     print(i)