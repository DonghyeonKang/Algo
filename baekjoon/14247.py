# 나무 자르기

# 그 날에 가장 많이 자라있는 나무 자르는 것
# 입력 받음 
# 아래를 n회 반복함 
#   나무 리스트에 하룻밤 자라는 길이를 모두 더해준다. (loop)
#   나무 리스트에서 가장 큰 값을 구해 result에 더해줌
# result 출력한다. 

# 가장 자라는 속도가 빠른 걸 가장 적은 횟수로 자르는 것.
# 입력 받음
# 자라는 속도를 기준으로 정렬함 
# 초기 길이와 자라는 속도 * 놔둔 날짜를 곱함
# 출력

import sys

n = int(sys.stdin.readline())
tree = [int(x) for x in sys.stdin.readline().split()]
growing = [int(x) for x in sys.stdin.readline().split()]
result = sum(tree)

growing.sort()
for i, data in enumerate(growing):
    result += i * data

print(result)

