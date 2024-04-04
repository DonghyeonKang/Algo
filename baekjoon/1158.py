n, k = map(int, input().split())

a = [i for i in range(1, n + 1)]
pointer = 0
result = []

while(a):
    cnt = 0
    while(cnt < k):
        pointer += 1
        if pointer > len(a):
            pointer = 1
        cnt += 1 
    result.append(str(a.pop(pointer - 1)))
    pointer -= 1

print("<" + ", ".join(result) + ">")