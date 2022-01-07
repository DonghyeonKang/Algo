# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
a = int(input())
num = []

num.append(input().split())
for i in range(a):
    num[0][i] = int(num[0][i])

num[0].sort()
print(num[0][0], num[0][a - 1])

# 1. num 리스트가 왜 2차원으로 되는 지
# 2. 바로 int로 받을 수 없는 지
# 3. 최댓값 최솟값 직접 짜보기
