
while(True):
    name, a, b = input().split()
    if name == "#" and a == "0" and b == "0":
        break
    
    if int(a) > 17 or int(b) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")