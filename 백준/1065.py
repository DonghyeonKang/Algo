# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
import sys

def compare(realnum):
    numlist = list(str(realnum))

    #a를 구한다
    a = int(numlist[0])

    #d를 구한다
    try:
        d = int(numlist[1]) - a 
    except: #out of index
        d = 0

    #n을 구한다
    n2 = len(numlist) 

    #구한 a, d, n으로 수를 만들고 realnum과 clonenum을 비교한다. 
    clonenum = []
    for i in range(n2):
        clonenum.append(str(a + i * d))
    if str(realnum) == ''.join(clonenum):
        return True
    else:
        return False

## main ##
n1 = int(sys.stdin.readline().rstrip()) 
count = 0

for i in range(n1): 
    count += compare(i + 1)
print(count)

#1. for 의 i값에서 a, d, n을 구해서 한수를 만들어 i와 비교한다. 
#2. 처음 생각했을 땐 괜찮았는데, 막상 짜보니 더럽다. 
#3. 문제 의도와는 다르게 1위는 sum안에 삼항 연산자에 수식과 반복문을 넣어 만들었다. 나보다 메모리를 많이 먹지만, 코드가 짧고, 속도가 빠르다. 
#4. 1위처럼 만들어보자. 