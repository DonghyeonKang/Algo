# 볼링공 고르기
# 볼링공의 개수 n과 볼링공의 무게 m개와 각 볼링공이 주어질 때, 2명의 플레이어가 서로 다른 무게를 고를 경우의 수를 고르시오
# 단, 무게가 같아도 다른 볼링공으로 간주한다. 

# 입력을 받는다. 
# 각 볼링공의 무게를 구한다.
# for loop 을 9회 돌며 sum(list[i:])을 result에 더한다. 
# result 를 출력한다. 

n, m = map(int, input().split())
numList = [int(x) for x in input().split()]

countList = [0 for i in range(10)]

for i in numList:
    countList[i - 1] += 1

result = 0
for i in range(9) :
    result += countList[i] * sum(countList[i + 1:])