# contact

n = int(input())
testCase = []

for i in range(n):
    testCase.append(list(input()))

for i in range(n):
    flag = 0
    pointer = 0
    while pointer <= len(testCase[i]):
        # 100+1+ 일때
        if testCase[i][pointer] == '1':
            pointer += 1
            cnt = 0
            while testCase[i][pointer] == '0':
                pointer += 1
                cnt += 1
            if cnt < 2:
                flag = 1
                break
            if testCase[i][pointer] == '1':
                while testCase[i][pointer] == '1':
                    pointer += 1
            else:
                flag = 1
                break

        # (01)+
        if testCase[i][pointer] == '0':
            pointer += 1
            if testCase[i][pointer] == '1':
                pointer += 1
                continue
            else:
                flag = 1
                break

    if flag == 1:
        print("NO")
    else:
        print("YES")