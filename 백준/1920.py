n = int(input())
v1 = sorted(list(map(int, input().split())))
m = int(input())
v2 = list(map(int, input().split()))

for i in v2:
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if v1[mid] == i:
            print(1)
            break
        elif v1[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    if left > right:
        print(0)