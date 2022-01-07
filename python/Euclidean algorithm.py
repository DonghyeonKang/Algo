numlist = list(map(int, input().split()))
numlist.sort()
r = numlist[1] % numlist[0]
numlist[1] = numlist[0]

while(1):
    if numlist[1] % r == 0:
        break
    r = numlist[1] % r
    numlist[1] = numlist[0]

print(r)