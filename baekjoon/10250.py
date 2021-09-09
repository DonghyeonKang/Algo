count = int(input())
customers = []
rooms = []

for i in range(count):
    customers.append(list(map(int, input().split())))


for i in range(count):
    room = customers[i][2] // customers[i][0] + 1
    floor = customers[i][2] % customers[i][0]
    if floor == 0:
        room -= 1
        floor = customers[i][0]
    tmp = str(floor)
    if room < 10:
        tmp += '0'
    tmp += str(room)
    rooms.append(tmp)

for i in range(count):
    print(rooms[i])