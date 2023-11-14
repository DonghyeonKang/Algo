# import sys

# a = list(sys.stdin.readline().upper())
# count = []
# max = 0

# for i in range(len(a)):
#     count.append(a[i:].count(a[i]))
#     if max < count[i]:
#         max = count[i]

# if count.count(max) > 1:
#     print('?')
# else:
#     print(a[count.index(max)])

#1. 시간초과

voca = input().upper()
essense = list(set(voca))

cnt = []
for i in essense:
    cnt.append(voca.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(essense[cnt.index(max(cnt))])

#1. 통과
