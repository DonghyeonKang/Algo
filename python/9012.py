n = int(input())
v = []

for i in range(n):
    v.append(list(input()))

for i in range(n):
    arr = []
    limit = len(v[i])
    if len(v[i]) > 1:
        top = 0
        arr.append(0)
        for j in range(0, limit):
            if arr[top] == v[i][j]:    
                arr.append(v[i][j])
                top += 1
            elif arr[top] == ")" or arr[top] == 0:
                arr.append(v[i][j])
                top += 1
            else:
                arr.pop()
                if top != 0:
                    top -= 1

    if len(arr) > 1:
        print("NO")
    else:
        print("YES")
