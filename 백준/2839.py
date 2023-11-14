num = int(input())  

quotient_5 = int(num / 5)   
remains_5 = num % 5     

if remains_5 == 0:      # 5로 나눈 나머지가 0이면 최대 개수
    result = quotient_5
elif num == 4 or num == 7 or num < 3:   # 나눌 수 없는 수 1, 2, 4, 7
    result = -1
else:
    for i in range(quotient_5 + 1):     # 5의 개수를 하나씩 줄여가며 나머지를 3으로 나누어본다. 
        tmp = num - (quotient_5 - i) * 5    
        quotient_3 = int(tmp / 3)   
        remains_3 = tmp % 3
        if remains_3 == 0:
            result = quotient_3 + (quotient_5 - i)  # 3으로 나눈 나머지가 0이면 최대 개수
            break

print(result)