# enumerate
a = [[1, 2], [3, 4], [5, 6]]
for i, j in enumerate(a):
    print(i, end=" ")
    print(j)

# 리스트 정수 요소 제거
aaa = [1, 2, 3]
aaa.remove(1)
print(aaa)

print("---------")
# 형식 지정자
a = 1
b = 2
print('%d %d' % (a, b))

# 파이썬 2중 리스트 요소 접근

a = '123X0000X0'
s = a.split('X')
print(s[0][1])

# 실험은 완벽했다!
# 문자열 함수 

# split의 인수가 문자열에 없으면
a = '123X0000X0'
s = a.split('o')
print(s)
# 그냥 리스트로 변한다. 

# 2차원 리스트 함수

array = [[1, 2, 3], [4, 5, 6]]
n = array[0].pop(0)

print(n)
# OK

print('%')

# print 사이 공백 제거하기
n = 1.22
print('%.2f' % n, '%', sep = '')
# ok

# 아스키 코드는 int형인가?

a = "a"

print(2 + ord(a))
# 맞다

# 리스트에서 요소 찾기
b = [1, 2]

if 1 in b:
    print('있다')
else:
    print('없다')
#okay

#list 자료형 변경
c = ['a', 'b', 'c']
d = list(map(ord, c))
print(d)
#okay


# 재귀함수 
def add(num):
    num += 1
    if num == 10:
        return num
    result = add(num) + num
    return result

print("--구분선--")
a = add(0)
print(a)