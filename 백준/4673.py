# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

def ans(n): #n 은 문자열로 받아야 한다. 
    numlist = list(str(n))
    sum = 0 #자릿수 합
    for i in numlist:
        sum += int(i)
    dn = n + sum #d(n)을 구한다
    if dn > 10000:  #d(n)이 10000보다 커지면 종료
        return;
    try:
        num.remove(dn)  #1~ 10000까지 수 중에서 d(n)을 제거한다
    except:
        return;
    ans(dn) #재귀함수

### main ###
num = []
for i in range(10000):
    num.append(i + 1)

for i in num:
    ans(i)

for i in num:
    print(i)


# 1. ValueError: list.remove(x): x not in list == 중복된 수 처리. 이미 지워진 수를 또 지우게 됨 -> try: except:로 예외처리
# 2. 더 효율적인 방법이 있을 듯 하다. 