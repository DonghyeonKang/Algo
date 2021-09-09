while(1):
    num = input()       # 숫자 받고
    tmp = list(num)     # tmp에 리스트로 복사한 다음
    tmp.reverse()       # 뒤집고
    tmp = "".join(tmp)  # 합치고 
    
    if num == '0': # 종료조건
        break
    elif num == tmp:    # 비교한다.
        print('yes')
    else:
        print('no')