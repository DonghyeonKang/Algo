import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    arr = sorted(arr)
    minus = n * 0.15
    if minus >= (int(minus) + 0.5):
        minus = int(minus) + 1
    else:
        minus = int(minus)

    result = sum(arr[minus:len(arr) - minus]) / (n - 2 * minus)
    if result >= (int(result) + 0.5):
        result = int(result) + 1
    else:
        result = int(result)

    print(result)