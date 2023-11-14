# 한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

alist = list(map(int, input().split()))
blist = []

for i in range(len(alist)):
    if i <= 1:
        blist.append(alist[i])
    else:
        blist.append(alist[i] - alist[i - 2])
blist.sort()

print(blist[0])
