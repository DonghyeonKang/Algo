import sys

while 1:                         
    try:
        a = sys.stdin.readline().strip()
        if len(a) == 0 :
            break
        print(a)    
    except:
        break