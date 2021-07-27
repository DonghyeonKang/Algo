a = [8, 23, 121, 21, 4]
key = 0
n = 1
while(n < len(a)):  # key 값
    key = a[n]
    tmp = n - 1
    while(tmp >= 0):    # 정렬
        if(key < a[tmp]): 
            a[tmp + 1] = a[tmp]
            a[tmp] = key
        tmp -= 1
    n += 1

print(a)