# 톱니바퀴

# 함수1 : 왼쪽 로테이션
# 함수2 : 오른쪽 로테이션

# 입력 받음 
# 2 -1 , 3 1
# n = 2 번 아래를 반복:
#   3번 아래를 반복:
#       j 번째 기어가 j + 1 과 다르면 연결 추가
#   if index % 2 == tries[0] % 2:
#       connect 에 tries[1] 추가
#       
#   tries[0] 이하 리스트 반복

# 정답 계산

import sys

def rotation(gear, flag):
    if flag == 1:
        gear.insert(0, gear.pop(len(gear) - 1))
    else:
        gear.append(gear.pop(0))


gears = []
for i in range(4):
    gears.append(list(input()))
n = int(sys.stdin.readline())
tries = []
for i in range(n):
    tries.append(list(map(int, sys.stdin.readline().split())))


# 결과 더하기
sumResult = 0
for i in range(4):
    rotation(gears[i], rotationList[i])
    if int(gears[i][0]) == 1:
        tmp = 1
        for j in range(i):
            tmp *= 2
    sumResult += tmp

print(sumResult)