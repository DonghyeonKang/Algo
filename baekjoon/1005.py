import sys 

# 입력
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    building = [[] for _ in range(n)]
    degree = [0 for _ in range(n)]
    wait = list(map(int, sys.stdin.readline().split()))
    v = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    w = int(sys.stdin.readline())

    # 차수, 노드
    for s, e in v:
        degree[e - 1] += 1
        building[s - 1].append(e)

    # 시작 노드
    stk = []
    for i in range(n):
        if degree[i] == 0:
            stk.append(i + 1)

    # 반복
    result = wait.copy()
    while(stk):
        # 종료 조건
        if w in stk:
            break

        # 스택 비우고 연결된 노드 넣기
        tmp = []
        for node in stk:
            for i in building[node - 1]:
                degree[i - 1] -= 1
                # 시간 누적
                a = wait[i - 1] + result[node - 1]
                result[i - 1] = max(a, result[i - 1])

                if degree[i - 1] == 0:
                    tmp.append(i)
        stk = tmp

    print(result[w - 1])
