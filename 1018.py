# 1. 입력 값을 받는다. 
# 2. 크기에 해당하는 체스판 2개를 만든다. 
# 3. 입력된 판과 체스판을 비교하여, 일치하는 부위는 1, 일치하지 않는 부위는 0으로 두 개의 비교 비교 판을 만든다. 
# 4. 두 비교판에서 8*8의 크기에 해당하는 값의 크기가 가장 큰 위치에서 최솟값을 구한다. 

# ---- main ----
# 입력
y, x = map(int, input().split(" "))
board = []
for i in range(y):
    board.append(input())

# 대조군 생성
contrast_W = []
contrast_B = []

for i in range(y):
    tmpstring = ""
    for j in range(x):
        if i % 2 == 1:        
            if j % 2 == 1:  # 홀수
                tmpstring += "W"
            if j % 2 == 0:  # 짝수
                tmpstring += "B"
        else:   
            if j % 2 == 1:  # 홀수
                tmpstring += "B"
            if j % 2 == 0:  # 짝수
                tmpstring += "W"

    contrast_W.append(tmpstring)

for i in range(y):
    tmpstring = ""
    for j in range(x):
        if i % 2 == 1:        
            if j % 2 == 1:  # 홀수
                tmpstring += "B"
            if j % 2 == 0:  # 짝수
                tmpstring += "W"
        else:   
            if j % 2 == 1:  # 홀수
                tmpstring += "W"
            if j % 2 == 0:  # 짝수
                tmpstring += "B"
    contrast_B.append(tmpstring)

# 입력된 체스판과 대조군과 비교하여 비교체스판 생성
compare_W = []
compare_B = []

for i in range(y):
    tmplist = []
    for j in range(x):
        if board[i][j] == contrast_W[i][j]:
            tmplist.append(0)
        else:
            tmplist.append(1)
    compare_W.append(tmplist)

for i in range(y):
    tmplist = []
    for j in range(x):
        if board[i][j] == contrast_B[i][j]:
            tmplist.append(0)
        else:
            tmplist.append(1)
    compare_B.append(tmplist)

# 최솟값구하기
result = 65
for i in range(x - 7):
    for j in range(y - 7):
        tmpresult = 0
        for k in range(8):
            tmpresult += sum(compare_W[j + k][i:i + 8])
        if result > tmpresult:
            result = tmpresult

for i in range(x - 7):
    for j in range(y - 7):
        tmpresult = 0
        for k in range(8):
            tmpresult += sum(compare_B[j + k][i:i + 8])
        if result > tmpresult:
            result = tmpresult

print(result)
