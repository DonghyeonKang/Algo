# 카운팅 정렬
import sys
numlist = []
count = int(sys.stdin.readline())

for i in range(count):
    num = int(sys.stdin.readline())

    if num >= len(numlist): #num이 리스트 개수보다 많을 때는 리스트를 늘린다 
        for i in range(num - len(numlist) + 1):
            numlist.append(0)
    if num < len(numlist): #리스트의 num 인덱스의 카운트를 올린다. 
        numlist[num] += 1

for index, num in enumerate(numlist):
    if num != 0:
        for i in range(num):
            print(index)
# 메모리 8MB에 걸림. 
# 카운팅 정렬이라는 걸 해봐야할 듯