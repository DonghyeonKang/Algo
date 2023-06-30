# 빵집
# 2차원 배열로 입력을 받는다. 
# dfs 함수를 구현한다. -> 탐색은 재귀함수로 구현된다. 방문한 노드는 X 값을 넣는다. 
# 모든 왼쪽 점에서 아래를 반복한다. 
#   dfs 의 리턴 값이 True 이면, result += 1 
# result 값 출력

r, c = map(int, input().split())

ground = []
for i in range(r):
    ground.append(list(input()))


def dfs(y, x):
    # ground 를 벗어나면 바로 리턴
    if x <= -1 or x > c or y <= -1 or y > r - 1:
        return False

    # 마지막 라인 도착
    if x == c:
        return True
    # 방문 노드일 시 바로 리턴
    if ground[y][x] == 'x':
        return False

    # 방문 처리
    ground[y][x] = 'x'

    if dfs(y - 1, x + 1): # 우상
        return True
    elif dfs(y, x + 1): # 우
        return True
    else:
        return dfs(y + 1, x + 1) # 우하

result = 0
for i in range(r):
    if dfs(i, 0):
        result += 1

print(result)