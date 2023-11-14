# 핸드폰 번호 궁합

num = []
for i in range(2):
    num.append(list(input()))

goong = []
for i in range(8):
    goong.append(num[0][i])
    goong.append(num[1][i])

while(len(goong) > 2):
    tmp = []
    for i in range(1, len(goong)):
        tmp.append((int(goong[i - 1]) + int(goong[i])) % 10)
    goong = tmp

print("".join(list(map(str, goong))))
