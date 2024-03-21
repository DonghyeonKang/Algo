import sys
n = int(sys.stdin.readline())
v = []
queue = []
back = -1

for i in range(n):
    v = sys.stdin.readline().split()
    if v[0] == "push":
        queue.append(v[1])
        back += 1
    elif v[0] == "pop":
        if back == -1:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
            back -= 1
    elif v[0] == "size":
        print(back + 1)
    elif v[0] == "empty":
        if back == -1:
            print(1)
        else:
            print(0)
    elif v[0] == "front":
        if back == -1:
            print(-1)
        else:
            print(queue[0])
    elif v[0] == "back":
        if back == -1:
            print(-1)
        else:
            print(queue[back])
