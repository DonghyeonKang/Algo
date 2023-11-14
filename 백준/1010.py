# 다리 놓기
import math

n = int(input())
test = []
for i in range(n):
    test.append(list(map(int, input().split())))

result = []
for i in test:
    if i[0] <= i[1]:
        result.append(int(math.factorial(i[1]) / (math.factorial(i[1] - i[0]) * math.factorial(i[0]))))
    else:
        result.append(int(math.factorial(i[0]) / (math.factorial(i[0] - i[1]) * math.factorial(i[1]))))

for i in result:
    print(i)