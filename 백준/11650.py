from typing import Coroutine


n = int(input())
coordinate = []

for i in range(n):
    coordinate.append(list(map(int, input().split(" "))))
coordinate = sorted(coordinate)     #sorted는 배열의 모든 요소를 고려하여 정렬한다. 
for i in coordinate:
    print("%d" %i[0] + " "+ "%d" %i[1])

# 추가 조건 내부 함수를 사용 금지