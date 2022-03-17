import sys

n = int(sys.stdin.readline())

v = []
deque = []
top = -1

for i in range(n):
    v = sys.stdin.readline().split()
    if v[0] == "push_front":
        deque.insert(0, v[1]) 
        top += 1       
    elif v[0] == "push_back":
        deque.append(v[1])
        top += 1
    elif v[0] == "pop_front":
        if top == -1:
            print(-1)
        else:             
            print(deque[0])
            del deque[0]
            top -= 1
    elif v[0] == "pop_back":
        if top == -1:
            print(-1)
        else:
            print(deque.pop())
            top -= 1
    elif v[0] == "size":
        print(top + 1)
    elif v[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    elif v[0] == "front":
        if top == -1:
            print(-1)
        else:
            print(deque[0])
    elif v[0] == "back":
        if top == -1:
            print(-1)
        else:       
            print(deque[top])