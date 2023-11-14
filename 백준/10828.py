import sys

n = int(sys.stdin.readline())
stack = []
top = -1
for i in range(n):
    v = sys.stdin.readline().split()
    if v[0] == "push":
        stack.append(v[1])
        top += 1
    elif v[0] == "pop":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            del stack[top]
            top -= 1
    elif v[0] == "size":
        print(top + 1)
    elif v[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    elif v[0] == "top":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
