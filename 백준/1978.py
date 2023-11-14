# 소수 찾기
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

cnt = 0
n = int(input())
numlist = list(map(int, input().split(" ")))

for i in numlist:
    limit = i
    if i != 1:
        flag = 0
        for j in range(2, limit):            
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            cnt += 1

print(cnt)