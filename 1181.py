# 1. 입력을 받는다. 
# 2. 리스트에 [길이, 단어] 추가한다. 
# 3. 정렬하며 출력한다. 

num = int(input())
words = [[0]]

for i in range(num):
    a = 2
    tmpword = input()

    for j in range(len(words)):
        if tmpword in words[j]:     # 중복 방지
            a = 1
            continue
        if len(tmpword) == words[j][0]:     # 기존의 리스트에 입력 받은 단어 길이에 해당하는 숫자가 존재하면
            words[j].append(tmpword)
            a = 0

    if a == 1:      # 중복 방지
        continue
    elif a == 2:
        words.append([len(tmpword), tmpword])

words.sort()

for i in range(1, len(words)):
    words[i].remove(words[i][0])
    words[i].sort()
    for j in range(len(words[i])):
        print(words[i][j])