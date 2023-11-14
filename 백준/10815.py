n = int(input())
a = list(map(int, input().split()))
# a 를 이진 트리 형태로 삽입

m = int(input())
b = list(map(int, input().split()))

def bs(arr, num):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid -1

    return False

a.sort()

r = []
for i in range(m):
    if bs(a, b[i]):
        r.append('1')
    else:
        r.append('0')

print(" ".join(r))