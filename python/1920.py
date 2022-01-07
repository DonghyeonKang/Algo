# 입력 받은 리스트를 정렬 후 탐색, 정렬되지 않은 상태로 탐색

# def binarySearch(datalist, num):
#     while(len(datalist) > 0):   # datalist 의 길이가 없어지면 종료
#         idx = len(datalist) // 2
#         if(datalist[idx] == num):   # 값을 찾으면 1
#             return 1
#         elif(datalist[idx] > num):  # 찾는 값이 idx가 가리키는 값보다 작을 경우
#             datalist = datalist[:idx]
#         else:  # 찾는 값이 idx가 가리키는 값보다 클 경우
#             datalist = datalist[idx + 1:]
#     return 0   # 값이 없으면 0

datanumcnt = int(input())
datalist = list(map(int, input().split(" ")))

positivetmplist = [0]
positivetmplistlength = 0
negativetmplist = [0]
negativetmplistlength = 0

for i in datalist:
    if i < 0:
        if negativetmplistlength < i:
            for j in range(i - negativetmplistlength):
                negativetmplist.append(0)
                negativetmplistlength += 1
            negativetmplist[-negativetmplistlength] = 1
        else:
            print(-i)
            negativetmplist[-i] = 1        
    else:
        if positivetmplistlength < i:
            for j in range(i - positivetmplistlength):
                positivetmplist.append(0)
                positivetmplistlength += 1
            positivetmplist[positivetmplistlength] = 1
        else:
            positivetmplist[i] = 1

findnumcnt = int(input())
numfind = list(map(int, input().split(" ")))

for i in numfind:
    if i >= 0:
        if i <= positivetmplistlength:
            print(positivetmplist[i])
        else:
            print(0)
    if  i < 0:
        if -i <= negativetmplistlength:
            print(negativetmplist[-i])
        else:
            print(0)
