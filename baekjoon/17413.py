# 문자열 뒤집기
# 포인터가 1씩 증가하며 아래를 반복
#   1. 열린 괄호라면
#       포인터 현재로 이동
#       zone = true
#   2. 닫힌 괄호라면
#       zone = false
#   zone 이 아니면서 공백이라면
#       포인터에서 지금까지 잘라서 뒤집고 결과에 추가
#       포인터 현재 +1 이동
#   Zone 이 아니면서 끝이라면
#       포인터에서 지금까지 잘라서 뒤집고 결과에 추가

s = list(input())
point = 0
result = []
zone = False
for i in range(len(s)):
    # 태그 시작
    if s[i] == '<':
        tmp = s[point:i].copy()
        tmp.reverse()
        result.append("".join(tmp))   
        zone = True

    # 태그 내에 문자
    if zone:
        result.append(s[i])

    # 태그 닫혔을 때
    if s[i] == '>':
        zone = False
        point = i + 1
        continue
    
    # 공백 나왔을 때
    if not zone and s[i] == ' ':
        tmp = s[point:i].copy()
        tmp.reverse()
        result.append("".join(tmp))
        result.append(' ')
        point = i + 1    
    
    # 마지막
    if not zone and i == (len(s) - 1):
        tmp = s[point:i + 1].copy()
        tmp.reverse()
        result.append("".join(tmp))

print("".join(result))