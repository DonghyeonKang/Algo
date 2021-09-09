# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

num = []
remainder = []
count = 10
for i in range(10):
    num.append(int(input()))
    remainder.append(num[i] % 42)

for i in remainder:
#    print(i)
    for j in remainder[remainder.index(i) + 1:]:
#        print(remainder[remainder.index(i) + 1:])
        if j == i:
            count -= 1
            remainder.remove(i)
#print(remainder)

print(count)

#1. 2중 for문의 range 교정 필요 - i -> 2스킵
#2. 분명 2를 확인 안 하는데, 왜 정답일까.
