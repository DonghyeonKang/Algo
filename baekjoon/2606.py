# 바이러스

# 입력 받음
# 인접 리스트 방식으로 저장
n = int(input())
m = int(input())

computers = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)

stk = []
result = []
# 1부터 탐색
stk.append(1)
while(True):
    # pop
    num = stk.pop()
    result.append(num)

    # stk update -> 방문하지 않은 노드만 추가
    for i in computers[num]:
        if i not in result and i not in stk:
            stk.append(i)

    # stk 0이면 종료 -> 연결된 노드 없음
    if len(stk) == 0:
        break

print(len(result) - 1)