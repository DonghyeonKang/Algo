#"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
#"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
def sume(answer):
    score = 0

    for i in answer:
        n = i.count('O')
        score += int(n * (n + 1) / 2)
    return score

num = int(input())
score = []

for i in range(num):
    answer = input().split('X')
    score.append(sume(answer))
for i in range(num):
    print(score[i])



#1. unsupported operand type(s) for +: 'int' and 'str' sum 함수에서 에러가 난다. 모든 수는 정수이다. append의 인수가 함수인 것이 문제일까. > 파이썬 내장함수 sum이 있었다...  
