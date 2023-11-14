n = int(input())
data = []
rank = []
for i in range(n):
    data.append(list(map(int, input().split(" "))))

num = 1
for i in data:
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            num += 1
    rank.append(num)
    num = 1

for i in rank:
    print(i, end=" ")