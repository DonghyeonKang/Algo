n = int(input())

goalArr = [] # 4 3 6 8 7 5 2 1
for i in range(n):
    goalArr.append(int(input()))

tmpArr = []
resultArr = []

tmpNum = 1
tmpArr.append(tmpNum)
resultArr.append("+")
tmpNum += 1
tmpTop = 0


while(1):
    if len(goalArr) == 0 or n == tmpNum - 1 and tmpArr[len(tmpArr) - 1] != goalArr[0]:
        break
    elif tmpTop == -1 or tmpArr[tmpTop] != goalArr[0]:
        resultArr.append("+")
        tmpArr.append(tmpNum)
        tmpNum += 1
        tmpTop += 1    
    else:
        resultArr.append("-")
        tmpArr.pop()
        del goalArr[0]
        tmpTop -= 1

if tmpTop == -1:
    for i in resultArr:
        print(i)
else:
    print("NO")