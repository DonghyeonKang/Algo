n, m = map(int, input().split())
v = sorted(list(map(int, input().split())))
p = n - 1
sum = 0

if len(v) > 1:
    for i in range(1, n):
        sum += (v[p] - v[p - 1]) * i
        if sum >= m:
            print(v[p - 1] + (sum - m) // i)
            break
        p -= 1
    if sum == 0:    # 예외1. 모든 수가 같은 경우
        print(v[p] - m // n)
    elif sum < m:   # 예외2. sum이 m 보다 낮을 경우
        tmp = (m - sum) // n
        if (m - sum) % n > 0:   # 올림
            tmp += 1
        print(v[p] - tmp)
elif v[p] == 1:     # 예외3. 길이가 1인 나무 밖에 없을 때
    print(1)
else:       # 예외4. 나무가 1개 밖에 없을 떄
    print(v[0] - m)
