# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

while 1:
    try:
        S = input()
        if len(S) > 2:
            R, S = S.split(" ")
            S = list(S)
        elif len(S) < 1:
            break
        else:
            continue
    
        for i in S:
            print(i * int(R), end = "")
        print('')
    except:
        break


# 1. During handling of the above exception, another exception occurred: 값이 하나만 들어오면, map()이 중단되고 exception으로 넘어간다. 그래서 R이 정의되지 않았다. 
# while 1:
#     try:
#         R, S = map(str, input().split(" "))
#         S = list(S)
#         for i in S:
#             print(i * int(R), end="")
#     except: # value error 
#         if R >= 1: # R이 들어왔다면 진행
#             continue
#         else:
#             break; # 아무 값 없으면, 값이 많으면 종료
#--------------------------------------------------------------------
# 2. SyntaxError: unexpected EOF while parsing.> try except 문에서 except를 안 쓰면 구문오류 발생
# 3. map(str, input().split())에서 enter 값이 1개 값으로 인식되던데, 왜 len(S1) < 1 에서 참이될까. 
# 4. 