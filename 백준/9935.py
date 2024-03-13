import sys
s = list(sys.stdin.readline().rstrip())
b = sys.stdin.readline().rstrip()
stk = []

for i in s:
    stk.append(i)
    if len(stk) >= len(b):
        if ''.join(stk[len(stk) - len(b):]) == b:
            for _ in range(len(b)):
                stk.pop()

if len(stk) == 0:
    print('FRULA')
else:
    print("".join(stk))