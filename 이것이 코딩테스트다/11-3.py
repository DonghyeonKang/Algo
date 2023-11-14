# 문자열 뒤집기 
# 0과 1로 이루어진 문자열이 주어진다. 
# 연속된 하나 이상의 숫자를 뒤집어 동일한 숫자가 연속하도록 해야한다. 
# 연속된 숫자를 뒤집는 최소 횟수를 구하라

# 문자열을 입력받는다. 
# count 리스트를 [0, 0] 으로 선언한다. 
# loop 으로 입력받은 리스트가 모두 반복될 때까지 아래 내용을 반복한다. 
#   만약 리스트의 특정 인덱스의 요소 a가 앞선 인덱스의 수와 다르다면
#       count 리스트의 a 번째 인덱스 += 1
# count 리스트의 요소 중 작은 수 출력

s = list(map(int, input()))

count = [0, 0]
tmp = s[0]
count[tmp] += 1

for i in s[1:]:
    if tmp != i:
        count[i] += 1
        tmp = i

if count[0] < count[1]:
    print(count[0])
else:
    print(count[1])