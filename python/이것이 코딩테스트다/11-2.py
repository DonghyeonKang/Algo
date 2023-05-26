# 각자리가 숫자 0~9로 이루어진 문자열 s가 주어졌을 때
# 숫자 사이에 +, * 연산자를 넣어 가장 큰 수를 만드는 프로그램
# 단, 연산의 우선 순위는 항상 왼쪽에서 오른쪽으로 진행한다. 

# loop 내에서 숫자의 개수만큼 아래를 반복한다.
#   만약 숫자가 0 또는 1이거나 또는 sum이 2보다 작으면
#       sum에 더한다. 
#   아니면
#       sum에 곱한다. 


nums = list(map(int, list(input())))

sum = nums[0]
for num in nums[1:]:
    if num == 0 or num == 1 or sum < 2 and num == 2:
        sum += num
    else:
        sum *= num

print(sum)