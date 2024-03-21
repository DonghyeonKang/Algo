import sys

n = int(sys.stdin.readline())
cases = []
importance = []
queue = []

for i in range(n):
    cases.append(list(map(int, sys.stdin.readline().split())))
    importance = map(int, sys.stdin.readline().split())
    tmp = []
    for num, data in enumerate(importance):
        tmp.append([num, data])
    queue.append(tmp)

def findBigger(tmp, queue):
    for k in range(len(queue[num])):
        if tmp < queue[num][k][1]: # 우선순위가 더 크면
            return 1 # 1 반환
    return 0   # 2 반환 


for num, data in enumerate(cases):
    cnt = 1
    while(len(queue[num]) > 0):
        tmp = queue[num][0][1]   # 우선순위 
        if findBigger(tmp, queue):      # 큰 수가 있다면, 
            queue[num].append(queue[num][0])    # 가장 앞의 데이터를 뒤로 추가시킴
            del queue[num][0]       # 가장 앞의 데이터를 지움
        else:
            if(data[1] == queue[num][0][0]):    # 내가 알고자 했던 친구면, 
                print(cnt)      # 출력
                break
            else:
                del queue[num][0]       # 가장 앞의 데이터를 지움
                cnt += 1        # 카운팅
