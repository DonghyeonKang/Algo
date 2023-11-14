num = int(input())
data = []
for i in range(num):
    age, name = map(str, input().split(" "))
    data.append([int(age), i, name])
data = sorted(data)

for i in range(num):
    print(data[i][0], end=" ")
    print(data[i][2])