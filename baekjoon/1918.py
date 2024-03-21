import sys

s = list(sys.stdin.readline().rstrip())
stk = []
operator = ['+', '-', '*', '/', '(', ')']
result = ""

for i in range(len(s)):
    if s[i] not in operator:
        result += s[i]
    elif s[i] == '(':
        stk.append(s[i])
    elif s[i] == ')':
        while(stk):
            if stk[-1] == '(':
                stk.pop()
                break
            result += stk.pop()
    elif s[i] == '*' or s[i] == '/':
        while(stk):
            if stk[-1] == '*' or stk[-1] == '/':
                result += stk.pop()
            else:
                break
        stk.append(s[i])
    else: # +, -
        while(stk):
            if stk[-1] == '+' or stk[-1] == '-' or stk[-1] == '*'  or stk[-1] == '/':
                result += stk.pop()
            else:
                break
        stk.append(s[i])
while(stk):
    result += stk.pop()
print(result)