# DNA
import sys

# 입력 
n, m = map(int, sys.stdin.readline().rstrip().split())
dna = []
for i in range(n):
    dna.append(sys.stdin.readline().rstrip())

h = 0
r = []
for i in range(m):
    a = [0, 0, 0, 0]
    for j in range(n):
        if dna[j][i] == 'A':
            a[0] += 1
        elif dna[j][i] == 'C':
            a[1] += 1
        elif dna[j][i] == 'G':
            a[2] += 1
        elif dna[j][i] == 'T':
            a[3] += 1
            
    # 공동 1순위 처리
    b = a.index(max(a))

    if b == 0:
        r.append('A')
    elif b == 1:
        r.append('C')
    elif b == 2:
        r.append('G')
    elif b == 3:
        r.append('T')
    h += n - max(a)

print("".join(r))
print(h)
