# n = 500000 m = 500000 최대 2500억회
# 중복은 없나? 
# 1초에 약 8500만회 

# n을 돌며 딕셔너리에 키 벨류 형식으로 추가 최대 50만
# m을 돌며 딕셔너리에 저장된 값을 차례대로 출력 최대 50만
# 총 100만 1초 내에 가능 

n = int(input())
d = {}
data1 = input().split(" ")
for i in data1:
    if d.get(i):
        d[i] += 1
    else:
        d[i] = 1

m = int(input())
data2 = input().split(" ")
for i in data2:
    if d.get(i):
        print(d.get(i), end="")
        print(" ", end="")
    else:
        print(0, end="")
        print(" ", end="")

