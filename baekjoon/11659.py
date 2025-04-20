# 구간합 구하기 4
import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# 누적합 리스트 구하기
sum_arr = [nums[0]]

for i in range(1, n):
    sum_arr.append(sum_arr[i - 1] + nums[i])

# 테스트 케이스 실행
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sum_arr[j - 1])
    else:
        print(sum_arr[j - 1] - sum_arr[i - 2])