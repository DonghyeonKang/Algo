n = int(input())
data = []
for i in range(n):
    data.append(list(reversed(list(map(int, input().split(" "))))))

data = sorted(data)     #sorted는 배열의 모든 요소를 고려하여 정렬한다. 
for i in data:
    print("%d" %i[1] + " "+ "%d" %i[0])

# 1. x, y 위치를 바꿔서 정렬한 뒤, 출력을 반대로 한다. 
# 2. sort function을 만든다. 