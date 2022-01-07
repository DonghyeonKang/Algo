# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

a = int(input())
b = int(input())
c = int(input())
num = list(str(a * b * c))
count = []

for i in range(10):
    count.append(0)
    for j in num:
        if str(i) == j:
            count[i] += 1
for i in count:
    print(i)
