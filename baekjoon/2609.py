a, b = map(int, input().split(" "))
# 최대 공약수 GCF 최소 공배수 LCM
if a < b:
    for i in range(a):
        num = a - i
        if int(a % num) == 0:
            if int(b % num) == 0:
                GCF = num
                LCM = GCF * int(a / num) * int(b / num)
                break
elif a > b:
    for i in range(b):
        num = b - i
        if int(b % num) == 0:
            if int(a % num) == 0:
                GCF = num
                LCM = GCF * int(a / num) * int(b / num)
                break
else:
    GCF = LCM = a


print(GCF)
print(LCM)


