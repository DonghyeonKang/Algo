# A 와 B

s = input()
t = list(input())

while(len(s) != len(t)):
    last = t.pop()
    
    if last == 'B':
        t.reverse()

if s == ''.join(t):
    print(1)
else:
    print(0)

