import sys
n = int(sys.stdin.readline())

a = n % 4
if a == 0:
    c = n // 4
else:
    c = n // 4 + 1

s = "long "
print(s * c, end="")
print("int")