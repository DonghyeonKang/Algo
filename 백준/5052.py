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

# 정렬
for i in range(test):
    nums[i].sort()

# 결과
for i in range(test):
    tmp = nums[i][0]
    flag = True

    for j in range(1, len(nums[i])):
        if len(nums[i][j]) >= len(tmp) and tmp == nums[i][j][:len(tmp)]:
            print('NO')
            flag = False
            break
        tmp = nums[i][j]

    if flag:
        print('YES')