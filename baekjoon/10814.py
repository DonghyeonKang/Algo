num = int(input())
data = []
for i in range(num):
    age, name = map(str, input().split(" "))
    data.append((int(age), name))
print(data)