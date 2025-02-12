n = int(input())
binN = bin(n)
listN = list(map(int, list(str(binN[2:]))))
print(sum(listN))