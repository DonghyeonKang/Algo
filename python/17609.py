# 회문

n =int(input())
strings = []
for i in range(n):
    strings.append(list(input()))

result = []
for i in range(n):
    diff = 0
    start = 0
    end = len(strings[i]) - 1
    for j in range(len(strings[i]) // 2):
        # 다르면 diff += 1
        if strings[i][start] != strings[i][end]:
            if strings[i][start + 1] == strings[i][end] and strings[i][start + 2] == strings[i][end - 1]: # 앞에 걸 지워야 하면
                start += 1
            elif strings[i][start] == strings[i][end - 1] and strings[i][start + 1] == strings[i][end - 2] : # 뒤에 걸 지워야 하면 
                end -= 1
            elif len(strings[i]) == 4 and j > 0:
                start += 1
            else: # 둘 다 지워봐도 다르면 그냥 다른 거 
                diff = 2
            diff += 1

        # diff 가 2 이상이면 result = 2
        if diff > 1:
            result.append('2')
            break
        
        # 포인터 변경
        start += 1
        end -= 1

    if diff == 1:
        result.append('1')
    elif diff == 0:
        result.append('0')

print('\n'.join(result))