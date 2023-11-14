# 숫자 카드게임 
# 숫자가 쓰인 카드들이 n * m 형태로 놓여있다. n은 행개수, m은 열개수 의미한다. 
# 뽑고자하는 카드가 포함되어있는 행을 선택한다. 
# 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 선택해야한다. 
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다. 
 
# 1. 입력 값을 받는다. 
# 2. 행별로 min 값을 구해서 list 에 넣는다. 
# 3. list 에서 max 값을 넣는다. 

row, col = map(int, input().split())
arr = []
for i in range(row):
    arr.append([int(x) for x in input().split()])

mins = []
for i in arr:
    mins.append(min(i))

print(max(mins))