import sys

n = []
for i in range(0, 3):
    n.append(sys.stdin.readline().strip())

isNum = []

for i, num in enumerate(n):
    if num != 'Fizz' and num != 'Buzz' and num != 'FizzBuzz':
        isNum.append([i, int(num)])
        break

rNum = (3 - isNum[0][0]) + isNum[0][1]   

if rNum % 3 == 0 and rNum % 5 == 0:
    print('FizzBuzz')
elif rNum % 3 == 0 and rNum % 5 != 0:
    print('Fizz')
elif rNum % 3 != 0 and rNum % 5 == 0:
    print('Buzz')
else:
    print(rNum)