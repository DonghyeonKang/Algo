# 3중 for문
N, M = map(int, input().split(" ")) # 입력
num = list(map(int, list(input().split(" "))))
ans = 0
n = 1

for i in num:
    for j in num[n:]:   # num[n:] 중복 제거
        tmp = num[n:]
        tmp.remove(j)
        for k in tmp:   # tmp 중복 제거
            if (i + j + k) == M:   # 같으면 탈출
                ans = i + j + k
                break
            elif ans < (i + j + k) < M: # M 보다 작고 합이 가장 큰
                ans = i + j + k
    n += 1

print(ans)