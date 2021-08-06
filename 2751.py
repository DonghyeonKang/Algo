def quicksort(data, start, end):
    key = start
    i = key + 1
    j = end
    while(i <= j):      # i 와 j 가 같아질 때 까지
        while(key <= data[i]):
            i += 1
        while(key >= data[i]):
            j -= 1

        if data[i] > data[j]:
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp
        else:
            tmp = key
            key = data[i]
            data[i] = tmp

    quicksort(data, start, j - 1)
    quicksort(data, j + 1, end)

cnt = int(input())
num = []
for i in range(cnt):
    num.append(int(input()))

# num.sort()
# for i in num:
#     print(i)

quicksort(num, 1, len(num) - 1)
