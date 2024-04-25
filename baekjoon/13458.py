import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

result = 0
for i in range(n):
    tmp = a[i] - b # 총감독 
    result += 1

    if tmp > 0:
        result += (a[i] - b) // c # 부감독
        if (a[i] - b) % c > 0:
            result += 1 # 부감독

print(result)