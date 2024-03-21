# 그룹 단어 체커

# 문자열을 리스트로 만든다. 
# 반복문으로 리스트를 조회한다. 
#   스택의 마지막 문자와 비교하고, 다르면, pop 해서 그룹 리스트에 넣음
#   만약 조회한 값이 그룹 리스트에 있으면 브레이크 
#   같으면, 스택에 추가


n = int(input())
words = []
for i in range(n):
    words.append(list(input()))

stk = []
group = []
result = 0

for i in range(n):
    flag = True
    stk.append(words[i][0])
    for j in words[i][1:]:
        # 다르면 pop 후 append pop 시 이미 group 에 있으면 break
        if stk[-1] != j:
            tmp = stk.pop()
            if tmp in group:
                flag = False
                break
            group.append(tmp)
            stk.clear()
            stk.append(j)
        else:
            # 같으면 append
            stk.append(j)

    if len(stk) > 0:
        if stk.pop() in group:
            flag = False

    group = []
    if flag:
        result += 1

print(result)

        