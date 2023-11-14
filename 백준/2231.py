#어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 
#245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
#자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

decomnum = input() #분해합을 넣는다
result = 0 # 결과 값 넣는 변수 

for i in range(1, len(list(decomnum)) * 9 + 1):
    sum = num = int(decomnum) - (len(list(decomnum)) * 9 + 1 - i) # num 은 생성자 sum은 생성자에서 분해합을 구하게 될 변수이다. 
    if num < 0: continue # num이 음수면 생략 분해합 10의 생성자 범위는 10-18 ~ 10 까지 이다. 
    numlist = list(str(num))
    for j in numlist: # 후보 생성자 숫자에서 분해합 구하기 
        sum += int(j)
    if sum == int(decomnum): # 후보 생성자의 분해합이 decomnum 과 같으면, break
        result = num
        break;

if result == 0:
    print('0')
else:
    print(result)

# 분해합을 만들 수 있는 생성자의 범위는 분해합의 자릿수 * 9 이다. 예를 들어 분해합이 100의 자리 수 이면, 생성자는 (분해합 - (3 * 9 )) 에서 분해합 까지 이다. 
# 범위 내의 숫자들의 분해합을 모두 구해서 decomnum과 일치하는 가장 작은 숫자를 출력한다. 
# 생성자 범위를 더 줄이면 좀 더 효율적인 알고리즘이 될 것 같다. 