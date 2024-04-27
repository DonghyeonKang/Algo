import sys

n = int(sys.stdin.readline())
s = 0
r = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'add':
        s = s | (1 << int(command[1]))
    elif command[0] == 'check':
        if  s & (1 << int(command[1])) != 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'remove':
        s = s & ~(1 << int(command[1]))
    elif command[0] == 'toggle':
        s = s ^ (1 << int(command[1]))
    elif command[0] == 'all':
        s = s | (1 << 21) - 1
    elif command[0] == 'empty':
        s = 0