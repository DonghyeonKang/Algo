import sys
n = int(sys.stdin.readline())
v = []
d = {}
sum = 0

for i in range(n):
    tmp = int(sys.stdin.readline())
    sum += tmp
    v.append(tmp)
    if str(tmp) in d:
        d[str(tmp)] += 1
    else:
        d[str(tmp)] = 1

v = sorted(v)
sortedDic = sorted(d.items(), key=lambda x: x[1], reverse=True)
tmp = sortedDic[0][1]
mostFreq = []
for i in sortedDic:
    if tmp == i[1]:
        mostFreq.append(int(i[0]))
    else:
        break
mostFreq = sorted(mostFreq)

print(round(sum / n))
print(v[n // 2])
if len(mostFreq) > 1:
    print(mostFreq[1]) # 최빈값
else: 
    print(mostFreq[0])
print(v[n - 1] - v[0])