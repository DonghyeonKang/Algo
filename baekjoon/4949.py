
while(1):
    top = 0
    stk = ['']
    sent = input()
    if sent == '.':
        break
    
    for i in list(sent):
        if i == ')' and stk[top] == '(':
            stk.pop()
            top -= 1
        elif i == ']' and stk[top] == '[':
            stk.pop()
            top -= 1
        elif i == '(' or i == ')' or i == '[' or i == ']':
            stk.append(i)
            top += 1
    
    if top != 0:
        print('no')
    else:
        print('yes')
    