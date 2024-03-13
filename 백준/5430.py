import sys
t = int(sys.stdin.readline())

for i in range(t):
    method = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()

    arr = arr[1:len(arr) - 1]
    if len(arr) > 0:
        arr = arr.split(',')

    rFlag = False
    eFlag = False
    for j in method:
        if j == 'R':
            if rFlag:
                rFlag = False
            else:
                rFlag = True
        elif j == 'D' and len(arr) == 0 and not eFlag:
            print('error')
            eFlag = True
        elif j == 'D' and len(arr) > 0:
            if rFlag:
                del arr[-1]
            else:
                del arr[0]

    if len(arr) == 0:
        if not eFlag:
            print('[]')
    else:
        if rFlag:
            arr.reverse()
        print('[' + ",".join(arr) + ']')