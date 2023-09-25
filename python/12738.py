import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def bs(arr, num):
    start = 0
    end = len(arr)

    while(start < end):
        mid = (start + end) // 2
        if arr[mid] < num:
            if start == mid:
                break
            start = mid
        else:
            end = mid 
    return end

d = [a[0]]
l = 0
for i in range(1, n):
    if d[l] < a[i]:
        d.append(a[i])
        l += 1
    if d[l] > a[i]:
        idx = bs(d, a[i])
        d[idx] = a[i]

print(len(d))