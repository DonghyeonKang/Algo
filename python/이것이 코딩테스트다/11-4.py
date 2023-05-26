# 만들 수 없는 금액 
# N 개의 동전을 가지고 있습니다. 이때 N개의 동전으로 만들 수 없는 가장 작은 양의 정수 금액을 구하는 프로그램을 작성하세요

# 값을 입력 받는다. 
# 입력된 리스트 a를 정렬한다. 
# 리스트 a를 loop를 돌며 아래를 반복한다. 
#   만약 리스트의 마지막 요소가 i번째 요소와 다르다면 
#       리스트 b에 추가한다. 
#   리스트 b를 loop를 돌며 아래를 반복한다. 
#       리스트 b에 b의 j번째 요소와 a의 i번째 리스트를 더한 값을 추가한다. 
#   만약 리스트 b의 마지막 요소가 리스트의 길이와 다르다면 
#       리스트 b를 i번째부터 아래를 반복한다. 
#           만약 인덱스와 해당 인덱스의 값이 다르다면 
#               인덱스 값 출력
#       break

# 값을 입력 받는다. 
# target 값을 1로 초기화 한다. 
# 입력된 리스트를 loop 로 아래를 반복한다. 
#   리스트의 요소 i가 target 보다 크면
#       target을 출력한다. 
#       break
#   sum += i
#   target = sum + 1

n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()

target = 1
sum = 0

for i in nums:
    if i > target:
        print(target)
        break

    sum += i
    target = sum + 1
